from typing import List

from OsuFileParser.my_dataclasses.SliderObject import SliderObject


class SliderDataParser:
    @staticmethod
    def parse_slider_data(data_line: str) -> SliderObject:
        data_line = data_line.split(',')
        return SliderObject(time=int(data_line[2]), length=float(data_line[7]))

    @staticmethod
    def parse_sliders_data(data: str) -> List[SliderObject]:
        res: List[SliderObject] = []
        for line in data.split('\n'):
            res.append(SliderDataParser.parse_slider_data(line))
        return res
