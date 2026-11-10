import os
import regex as re
from app.core.env import configEnv
from app.utils.singleton import Singleton

class TeamMatcher(metaclass=Singleton):
    '''TeamMatcher'''
    __module__ = __name__
    __qualname__ = 'TeamMatcher'
    __doc__ = '\n    识别制作组、字幕组\n    '
    __release_groups: str = None
    pass


if __name__ == '__main__':
    matcher = TeamMatcher()
    print(matcher.match('钢铁侠-cmct.mkv'))
    print(matcher.match('钢铁侠-CMCTV.mkv'))
    print(matcher.match('钢铁侠-CMCTA.mkv'))
    print(matcher.match('Mr.Topaze.1961.1080p.Blu-ray.AVC.LPCM.2.0-BMDru'))
    print(matcher.match('Mr.Topaze.1961.1080p.Blu-ray.AVC.LPCM.2.0-神赫Parker@CHDBits'))
    print(matcher.match('Christiane.F.1981.UHD.BluRay.1080p.x265.10bit.DDP5.1.MNHD-FRDS.mkv'))
    print(matcher.match('Christiane.F.1981.UHD.BluRay.1080p.x265.10bit.DDP5.1-AJ@FRDS.mkv'))
    print(matcher.match('The.Apothecary.Diaries.S02E06.1080p.NF.WEB-DL.AAC2.0.H.264-MWeb.mkv'))
    print(matcher.match('Sonic.the.Hedgehog.3.2024.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-AQLJ@HDSky.mkv'))
    print(matcher.match('Sonic.the.Hedgehog.3.2024.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-doraemon.mkv'))
    print(matcher.match('Sonic.the.Hedgehog.3.2024.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-wezjh@OurBits.mkv'))
    print(matcher.match('Horrible.High.Heels.1996.USA.BluRay.1080p.AVC.LPCM.2.0-FFansDIY@至尊宝.iso'))
    print(matcher.match('A.Guilty.Conscience.2023.BluRay.AV1.12Bit.DDP(5.1).1080P-FFans@NXX'))
    print(matcher.match('A.Guilty.Conscience.2023.BluRay.AV1.12Bit.DDP(5.1).1080P-TnT'))
    print(matcher.match('A.Guilty.Conscience.2023.BluRay.AV1.12Bit.DDP(5.1).1080P-404.mkv'))

