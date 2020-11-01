# coding=utf-8
import wd

def f_style(data):
    print("穿衣风格分析开始......")
    print("穿衣方式：常规-经典-流行-未来-独特")
    st1 = {"常规": data[3], 
        "经典": data[2]+data[3], 
        "流行": data[1]+data[3], 
        "未来": data[1]+data[2], 
        "独特": data[0]+data[1]}
    print("可能会喜欢：", max(st1, key=lambda i: st1[i]))

    print('～'*50)
    print("注重点：衣服-包-鞋子-首饰-眼镜-围巾/领带")
    st2 = {"衣服": data[0]+data[3], 
        "包": data[4], 
        "鞋子": data[4]+data[5], 
        "首饰": data[3]+data[4], 
        "眼镜": data[2]+data[3], 
        "围巾/领带": data[2]+data[5]}
    print("可能会喜欢：", max(st2, key=lambda i: st2[i]))

    print('～'*50)
    print("关注点：发型-化妆-体型-健康-心态")
    st3 = {"发型": data[1]+data[4], 
        "化妆": data[0]+data[3], 
        "体型": data[3]+data[4], 
        "健康": data[0]+data[4], 
        "心情": data[1]+data[2]}
    print("可能会喜欢：", max(st3, key=lambda i: st3[i]))

    print('～'*50)
    print("款式：宽松-运动-休闲-商务-正装-礼服	")
    st4 = {"宽松": data[0]+data[2], 
        "运动": data[0]+data[5], 
        "休闲": data[1]+data[5], 
        "商务": data[3]+data[4], 
        "正装": data[2]+data[3], 
        "礼服": data[1]+data[3]}
    print("可能会喜欢：", max(st4, key=lambda i: st4[i]))

    print('～'*50)
    print("材料：人造-天然-混合-舒适")
    st5 = {"人造": data[3]+data[5], 
        "天然": data[3]+data[4], 
        "混合": data[2]+data[3], 
        "舒适": data[1]+data[3]}
    print("可能会喜欢：", max(st5, key=lambda i: st5[i]))

    print('～'*50)
    print("图案类型：字母-人物-花卉-几何-寓意")
    st6 = {"字母": data[2], 
        "人物": data[0], 
        "花卉": data[1], 
        "几何": data[2]+data[3], 
        "寓意": data[1]+data[2]}
    print("可能会喜欢：", max(st6, key=lambda i: st6[i]))

    print('～'*50)
    print("品牌需求：小众-独立-时尚-大众-个人喜好")
    st7 = {"小众": data[0]+data[4], 
        "独立": data[2], 
        "时尚": data[1]+data[3], 
        "大众": data[2]+data[3], 
        "无个人喜好": data[0]}
    print("可能会喜欢：", max(st7, key=lambda i: st7[i]))

    print('～'*50)
    print("线条类型：直-曲-波浪-折-弧-长-短-乱-规则")
    st8 = {"直": data[0]+data[5], 
        "曲": data[1], 
        "波浪": data[1]+data[5], 
        "折": data[2]+data[3], 
        "弧": data[1]+data[2], 
        "长": data[1]+data[4]+data[5],
        "短": data[0]+data[2]+data[3],
        "乱": data[1]+data[2], 
        "规则": data[2]+data[3]}
    print("可能会喜欢：", max(st8, key=lambda i: st8[i]))

    print('～'*50)
    print("几何类型：点-圆-椭圆-方-长方-三角-五角星-多角星-规则-不规则")
    st9 = {"点": data[0], 
        "圆": data[0]+data[1], 
        "椭圆": data[0]+data[1]+data[2],
        "方": data[2]+data[3], 
        "长方": data[1]+data[2]+data[3],
        "三角": data[2]+data[3]+data[4],
        "五角星": data[3]+data[4], 
        "多角星": data[4]+data[5], 
        "规则": data[2]+data[3], 
        "不规则": data[1]}
    print("可能会喜欢：", max(st9, key=lambda i: st9[i]))


if __name__ == "__main__":
    print("机器开始分析", "."*100)
    f_style(wd.new1)
