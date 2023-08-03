import copy
import pathlib
from typing import Tuple, List

from OsuFileParser import BeatmapFileParser, BeatmapData
from OsuFileParser.my_dataclasses.SliderObject import SliderObject
from OsuFileParser.my_dataclasses.TimingPoint import TimingPoint
from src.app_backend.slider_convertor_module.parsers.SliderDataParser import SliderDataParser
from src.app_backend.slider_convertor_module.parsers.TimingDataParser import TimingDataParser


def _timing_sort_key(timing_str: str):
    """Key to sort timing by 'time' and 'uninherited' in ascending order"""
    vals = timing_str.split(',')
    return int(vals[0]), int(vals[6])


def _create_timing_point_str(*, time: int, beat_length: float, uninherited: bool,
                             timing_example: TimingPoint = None) -> str:
    if timing_example is None:
        return f"{int(time)},{beat_length},{int(uninherited)}"
    else:
        res_timing_point = copy.deepcopy(timing_example)
        res_timing_point.time = time
        res_timing_point.beat_length = beat_length
        res_timing_point.uninherited = uninherited
        return str(res_timing_point)


def _arrange_slider(*, slider_tick_rate: float, beat_length: float, beatmap_sv: float, current_sv_multiplier: float,
                    new_end_ms: int, slider: SliderObject, timing_example: TimingPoint = None) -> (str, str):
    """Arranges slider, tries to include ZERO slider ticks in it."""
    start_ms = slider.time
    slider_length = slider.length
    old_slider_completion_time = slider_length / (100 * beatmap_sv * current_sv_multiplier) * beat_length
    new_slider_completion_time = new_end_ms - start_ms
    new_sv_multiplier = slider_tick_rate
    new_beat_length = new_slider_completion_time / old_slider_completion_time * \
                      beat_length * current_sv_multiplier / new_sv_multiplier
    # Avoiding slider ticks
    expected_slider_ticks = (new_end_ms - start_ms) * slider_tick_rate / new_beat_length
    if expected_slider_ticks > 1:
        new_beat_length *= expected_slider_ticks
        new_sv_multiplier *= expected_slider_ticks
    t1 = _create_timing_point_str(uninherited=True, time=start_ms, beat_length=new_beat_length,
                                  timing_example=timing_example)
    t2 = _create_timing_point_str(uninherited=False, time=start_ms, beat_length=(-100 / new_sv_multiplier),
                                  timing_example=timing_example)
    return t1, t2


class SliderConvertor:
    @staticmethod
    def convert_slider(*, slider_tick_rate: float, beat_length: float, beatmap_sv: float, current_sv_multiplier: float,
                       destination_ms: int, slider_data: str, timing_example_data: str) -> Tuple[str, str]:
        """
        Function that makes given slider end at the given destination_ms.
        Without a single tick in the slider.

        :param: slider_tick_rate: Slider tick rate.
        :param: beat_length: Beat length in ms.
        :param: beatmap_sv: Beatmap SV.
        :param: current_sv_multiplier: Current SV multiplier from inherited time point.
        :param: destination_ms: Slider end destination in ms.
        :param: slider_data: Slider data from .osu file.
        :param: timing_example_data: Timing example data.

        :return: Returns Tuple of inherited and inherited timing point as strings, specifying only beat length,
                 uninherited values.
        """
        if timing_example_data == "":
            slider = SliderDataParser.parse_slider_data(slider_data)
            return _arrange_slider(slider_tick_rate=slider_tick_rate, new_end_ms=destination_ms,
                                   beat_length=beat_length, beatmap_sv=beatmap_sv,
                                   current_sv_multiplier=current_sv_multiplier, slider=slider)
        else:
            slider = SliderDataParser.parse_slider_data(slider_data)
            timing_example = TimingDataParser.parse_timing_point(timing_example_data)
            return _arrange_slider(slider_tick_rate=slider_tick_rate, new_end_ms=destination_ms,
                                   beat_length=beat_length, beatmap_sv=beatmap_sv,
                                   current_sv_multiplier=current_sv_multiplier, slider=slider,
                                   timing_example=timing_example)

    @staticmethod
    def convert_sliders(*, slider_tick_rate: float, beat_length: float, beatmap_sv: float, current_sv_multiplier: float,
                        destination_ms: int, sliders_data: str, timing_example_data: str) -> List[str]:
        """
        Function that makes given sliders end at the given destination_ms.
        Fully depended on convert_slider function.
        """
        res: List[str] = []
        for slider_data in sliders_data.splitlines():
            t1, t2 = SliderConvertor.convert_slider(slider_tick_rate=slider_tick_rate, destination_ms=destination_ms,
                                                    beat_length=beat_length, beatmap_sv=beatmap_sv,
                                                    current_sv_multiplier=current_sv_multiplier,
                                                    slider_data=slider_data, timing_example_data=timing_example_data)
            res.append(t1)
            res.append(t2)
        res.sort(key=_timing_sort_key)
        return res

    @staticmethod
    def convert_sliders_with_osu_file(*, osu_file_path: pathlib.Path, destination_ms: int, sliders_data: str) -> \
            List[str]:
        """
        Function that makes given sliders end at the given destination_ms.
        Fully depended on convert_slider function.
        """
        res: List[str] = []
        beatmap_data = BeatmapData(filepath=str(osu_file_path.name),
                                   data=BeatmapFileParser.parse_full_osu_file(osu_file_path))
        slider_tick_rate = float(beatmap_data.difficulty.slider_tick_rate)
        beatmap_sv = float(beatmap_data.difficulty.slider_multiplier)

        timing_points_list = beatmap_data.timing_points
        cur_ind = 0  # pointer to the index of the timing list where time >= slider start time.
        beat_length = None
        current_sv_multiplier = 1
        timing_example = None
        for slider_data in sliders_data.splitlines():
            slider = SliderDataParser.parse_slider_data(slider_data)
            while cur_ind < len(timing_points_list) and timing_points_list[cur_ind].time <= slider.time:
                if timing_points_list[cur_ind].uninherited:
                    beat_length = timing_points_list[cur_ind].beat_length
                else:
                    current_sv_multiplier = (-100 / timing_points_list[cur_ind].beat_length)
                timing_example = timing_points_list[cur_ind]
                cur_ind += 1
            # print(f"{slider_tick_rate=}", f"{destination_ms=}", f"{beat_length=}", f"{beatmap_sv=}",
            #       f"{current_sv_multiplier=}", f"{timing_example=}", sep="\n")
            t1, t2 = _arrange_slider(slider_tick_rate=slider_tick_rate, new_end_ms=destination_ms,
                                     beat_length=beat_length, beatmap_sv=beatmap_sv,
                                     current_sv_multiplier=current_sv_multiplier,
                                     slider=slider, timing_example=timing_example)
            res.append(t1)
            res.append(t2)
        res.sort(key=_timing_sort_key)
        return res
