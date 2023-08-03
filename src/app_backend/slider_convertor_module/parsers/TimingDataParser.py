from typing import List

from OsuFileParser.my_dataclasses.TimingPoint import TimingPoint


def _create_timing_point_instance(l: List[str]) -> TimingPoint:
    converted_values = [int(l[0]), float(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), bool(l[6]), int(l[7])]
    instance = TimingPoint(*converted_values)
    return instance


class TimingDataParser:
    @staticmethod
    def parse_timing_point(data_line: str) -> TimingPoint:
        data_line = data_line.split(',')
        return _create_timing_point_instance(data_line)

    @staticmethod
    def parse_timing_points(data: str) -> List[TimingPoint]:
        res: List[TimingPoint] = []
        for line in data.split('\n'):
            res.append(TimingDataParser.parse_timing_point(line))
        return res
