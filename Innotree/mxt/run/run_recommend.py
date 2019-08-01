
import sys
sys.path.append("C:\\Users\\hasee\\PycharmProjects")

from Innotree.mxt.function.recommend import Recommend

baseinfo = Recommend().in_recommend()
quality = Recommend().write_com_baseinfo(baseinfo)
manage = Recommend().write_zizhi(quality)

finance = Recommend().write_jingying(manage)
admin = Recommend().write_caiwu(finance)
honor = Recommend().write_zongheguanli(admin)
pay = Recommend().write_rongyu(honor)
jiaofei = Recommend().write_jiaofei(pay)

success = Recommend().shenhe_reco(jiaofei)
fangtan_to_shenpi = Recommend().shenpi_to_fangtan(success)
shenpi_fangtan = Recommend().fangtan_to_shenpi(fangtan_to_shenpi)
Recommend().shenpi_fangtan_chenggong(shenpi_fangtan)
