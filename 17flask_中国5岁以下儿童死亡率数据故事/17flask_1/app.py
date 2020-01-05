import pandas as pd
from flask import Flask
from flask import render_template, request, redirect
from pyecharts import Map, Bar, Line, WordCloud

app = Flask(__name__)


@app.route('/')
def index():
    data1 = pd.read_csv(r"./static/data/1Child mortality in China.csv")
    data2 = pd.read_csv(
        r"./static/data/2Causes of death among rural children.csv")
    data3 = pd.read_csv(
        r"./static/data/3Causes of urban child death.csv")
    data4 = pd.read_csv(
        r"./static/data/4Number of disease prevention and control centers in China.csv")
    data5 = pd.read_csv(
        r"./static/data/5Number of specialist disease prevention hospitals in China.csv")
    data1_x = data1.columns.values
    data2_x = data2.columns.values
    data3_x = data3.columns.values
    data4_x = data4.columns.values
    data5_x = data5.columns.values

    data1_y = data1.values.tolist()
    data2_y = data2.values.tolist()
    data3_y = data3.values.tolist()
    data4_y = data4.values.tolist()
    data5_y = data5.values.tolist()
    return render_template("index.html", data1_x=data1_x[1:], data2_x=data2_x[1:], data3_x=data3_x[1:],
                           data4_x=data4_x[1:],
                           data5_x=data5_x[1:], data1_y=data1_y, data2_y=data2_y, data3_y=data3_y, data4_y=data4_y,
                           data5_y=data5_y, a=1)



@app.route('/bar')
def index_bar():
    data = pd.read_csv(r"static/data/1Child mortality in China.csv")
    columns = data.columns.values
    data = data.values.tolist()
    bar = Bar("2009-2018儿童死亡率", width="50%")
    bar.add(data[0][0], columns[1:], data[0][1:])
    for i in data[1:]:
        bar.add(i[0], columns[1:], i[1:])
    return render_template('index.html',
                           myechart=bar.render_embed(),
                           script_list=bar.get_js_dependencies(), text='''
                           从对比图看出，中国5岁以下儿童死亡率在过去10年间总体趋于下降，农村5岁以下儿童的死亡率一直以较大幅度高于城市同类儿童死亡率。
联系图表，可以发现2011年是一个节点年份，11年以后我国5岁以下儿童死亡率降幅明显。将此节点信息联系国务院在2011年根据我国儿童发展过程中面临的突出问题，针对性发布的《中国儿童发展纲要》可知，在2011年以来，我国在儿童相关的健康、福利、社会环境等领域有了长足发展。
该纲要首次将降低儿童死亡率作为儿童健康领域的主要目标之一，此外还在其他领域增补了大量与儿童安全相关的内容，包括强化国家和政府在不同类别弱势儿童保护方面的责任，建立和完善国家、省（自治区、直辖市）、市（区、县）三级儿童发展监测数据库。
从数据来看，这项举措的收效甚佳，相比于2011年，2018中国5岁以下儿童的死亡率下降了一半之多，虽然其中肯定包括了医疗水平不断提高等原因，但即使在城市地区，也成果喜人。
                           ''', text1='''这次项目的数据采集主要围绕中国儿童死亡情况展开，搜集了近10年来中国5岁以下儿童（包含全体、城市、农村）死亡率数据、其主要死因的分析数据及可能存在的预防控制和专科救助情况数据。
总体来说我国5岁以下儿童死亡率在医疗水平提高以及国家专项纲要推动等因素下已经实现较大幅度的降低，但是农村儿童较高的死亡率仍然可以作为儿童生命安全健康任务的核心突破点。而对于儿童生存环境中存在的各种危险因素，人们的重视程度还是不够，要切实解决这些危险问题，首要做到的就是具体情况具体分析，切不可以以偏概全，对于家庭因素、地区因素、环境因素都要点对点提出宣传及解决建议。而针对疾病预防控制中心及专科疾病防治院的发展，最大问题是发展遇到瓶颈，被暂时性的饱和假象拖慢了发展脚步。儿童的疾病防治与专科诊疗问题从来不是“医疗机构基本覆盖”、“救援需求基本满足”可以解决，更充分的发展，更尖端技术的推广仍然任重道远。''')


@app.route('/line')
def index_line():
    data = pd.read_csv(r"./static/data/1Child mortality in China.csv")
    columns = data.columns.values
    data = data.values.tolist()
    bar = Line("2009-2018儿童死亡率", width="50%")
    bar.add(data[0][0], columns[1:], data[0][1:])
    for i in data[1:]:
        bar.add(i[0], columns[1:], i[1:])
    return render_template('index.html',
                           myechart=bar.render_embed(),
                           script_list=bar.get_js_dependencies(), text='''
                           从图可以看出，中国5岁以下儿童死亡率在过去10年间总体趋于下降，农村5岁以下儿童的死亡率一直以较大幅度高于城市同类儿童死亡率。
联系图表，可以发现2011年是一个节点年份，11年以后我国5岁以下儿童死亡率降幅明显。将此节点信息联系国务院在2011年根据我国儿童发展过程中面临的突出问题，针对性发布的《中国儿童发展纲要》可知，在2011年以来，我国在儿童相关的健康、福利、社会环境等领域有了长足发展。
该纲要首次将降低儿童死亡率作为儿童健康领域的主要目标之一，此外还在其他领域增补了大量与儿童安全相关的内容，包括强化国家和政府在不同类别弱势儿童保护方面的责任，建立和完善国家、省（自治区、直辖市）、市（区、县）三级儿童发展监测数据库。
从数据来看，这项举措的收效甚佳，相比于2011年，2018中国5岁以下儿童的死亡率下降了一半之多，虽然其中肯定包括了医疗水平不断提高等原因，但即使在城市地区，也成果喜人。
                           ''', text1='''这次项目的数据采集主要围绕中国儿童死亡情况展开，搜集了近10年来中国5岁以下儿童（包含全体、城市、农村）死亡率数据、其主要死因的分析数据及可能存在的预防控制和专科救助情况数据。
总体来说我国5岁以下儿童死亡率在医疗水平提高以及国家专项纲要推动等因素下已经实现较大幅度的降低，但是农村儿童较高的死亡率仍然可以作为儿童生命安全健康任务的核心突破点。而对于儿童生存环境中存在的各种危险因素，人们的重视程度还是不够，要切实解决这些危险问题，首要做到的就是具体情况具体分析，切不可以以偏概全，对于家庭因素、地区因素、环境因素都要点对点提出宣传及解决建议。而针对疾病预防控制中心及专科疾病防治院的发展，最大问题是发展遇到瓶颈，被暂时性的饱和假象拖慢了发展脚步。儿童的疾病防治与专科诊疗问题从来不是“医疗机构基本覆盖”、“救援需求基本满足”可以解决，更充分的发展，更尖端技术的推广仍然任重道远。''')


@app.route('/word')
def word():
    time = request.args.get("time")
    prevention = request.args.get("city")
    if prevention == "1":
        return redirect("/word1?time={}".format(time))
    else:
        return redirect("/word2?time={}".format(time))


@app.route('/word1')
def index_word():
    time = request.args.get("time")
    data = pd.read_csv(
        r"./static/data/2Causes of death among rural children.csv")
    columns = data.columns.values
    data_x = data["死因"].values.tolist()
    data_y = data[time].values.tolist()
    print(data_y)
    word = WordCloud("{}农村儿童死亡原因".format(time), width="50%")
    word.add("", data_x, data_y)
    return render_template('index.html',
                           myechart=word.render_embed(),
                           script_list=word.get_js_dependencies(), text='''
                           从图来看，无论对于城市还是农村5岁以下儿童来说，损伤和中毒都是具有最高威胁性的，而这个首要死因反应出来的是对儿童生存环境的疏忽。而损伤和中毒这一死因进一步之后，结果令人咋舌，溺亡占比近50%、意外跌落占比近20%、交通意外占比近15%。
当今社会，几乎到处都存在着发生意外损伤的危险，环境中致意外损伤的危险因素也多种多样，并且存在差异，要防范儿童的不必要死亡必须深刻认识这一点。经济、交通落后的农村地区车祸死亡率高于经济、交通发达地区；考虑由于父母的文化程度低、多子女、对儿童照管不周以及缺乏安全教育，故农村儿童在交通上有更大的危险性；在水网地区车祸死亡率较低，但由于缺乏防护措施，溺水等发生则较高；一氧化碳中毒在农村多由于燃煤取暖所致，而在城市系热水器使用不当，未注意通风所致；由于电器的普及，电击伤呈上升趋势，多由于忽视安全操作所致。
只有针对性地分析这些可能存在的危险因素，才能真正意义上的保护儿童的生命安全健康。
                           ''', text1='''这次项目的数据采集主要围绕中国儿童死亡情况展开，搜集了近10年来中国5岁以下儿童（包含全体、城市、农村）死亡率数据、其主要死因的分析数据及可能存在的预防控制和专科救助情况数据。
总体来说我国5岁以下儿童死亡率在医疗水平提高以及国家专项纲要推动等因素下已经实现较大幅度的降低，但是农村儿童较高的死亡率仍然可以作为儿童生命安全健康任务的核心突破点。而对于儿童生存环境中存在的各种危险因素，人们的重视程度还是不够，要切实解决这些危险问题，首要做到的就是具体情况具体分析，切不可以以偏概全，对于家庭因素、地区因素、环境因素都要点对点提出宣传及解决建议。而针对疾病预防控制中心及专科疾病防治院的发展，最大问题是发展遇到瓶颈，被暂时性的饱和假象拖慢了发展脚步。儿童的疾病防治与专科诊疗问题从来不是“医疗机构基本覆盖”、“救援需求基本满足”可以解决，更充分的发展，更尖端技术的推广仍然任重道远。''')


@app.route('/word2')
def index_word_2():
    time = request.args.get("time")
    data = pd.read_csv(
        r"./static/data/3Causes of urban child death.csv")
    columns = data.columns.values
    data_x = data["死因"].values.tolist()
    data_y = data[time].values.tolist()
    print(data_y)
    word = WordCloud("{}城市儿童死亡原因".format(time), width="50%")
    word.add("", data_x, data_y)
    return render_template('index.html',
                           myechart=word.render_embed(),
                           script_list=word.get_js_dependencies(), text='''
                           从图来看，无论对于城市还是农村5岁以下儿童来说，损伤和中毒都是具有最高威胁性的，而这个首要死因反应出来的是对儿童生存环境的疏忽。而损伤和中毒这一死因进一步之后，结果令人咋舌，溺亡占比近50%、意外跌落占比近20%、交通意外占比近15%。
当今社会，几乎到处都存在着发生意外损伤的危险，环境中致意外损伤的危险因素也多种多样，并且存在差异，要防范儿童的不必要死亡必须深刻认识这一点。经济、交通落后的农村地区车祸死亡率高于经济、交通发达地区；考虑由于父母的文化程度低、多子女、对儿童照管不周以及缺乏安全教育，故农村儿童在交通上有更大的危险性；在水网地区车祸死亡率较低，但由于缺乏防护措施，溺水等发生则较高；一氧化碳中毒在农村多由于燃煤取暖所致，而在城市系热水器使用不当，未注意通风所致；由于电器的普及，电击伤呈上升趋势，多由于忽视安全操作所致。
只有针对性地分析这些可能存在的危险因素，才能真正意义上的保护儿童的生命安全健康。
                           ''', text1='''这次项目的数据采集主要围绕中国儿童死亡情况展开，搜集了近10年来中国5岁以下儿童（包含全体、城市、农村）死亡率数据、其主要死因的分析数据及可能存在的预防控制和专科救助情况数据。
总体来说我国5岁以下儿童死亡率在医疗水平提高以及国家专项纲要推动等因素下已经实现较大幅度的降低，但是农村儿童较高的死亡率仍然可以作为儿童生命安全健康任务的核心突破点。而对于儿童生存环境中存在的各种危险因素，人们的重视程度还是不够，要切实解决这些危险问题，首要做到的就是具体情况具体分析，切不可以以偏概全，对于家庭因素、地区因素、环境因素都要点对点提出宣传及解决建议。而针对疾病预防控制中心及专科疾病防治院的发展，最大问题是发展遇到瓶颈，被暂时性的饱和假象拖慢了发展脚步。儿童的疾病防治与专科诊疗问题从来不是“医疗机构基本覆盖”、“救援需求基本满足”可以解决，更充分的发展，更尖端技术的推广仍然任重道远。''')


@app.route('/city')
def index_city():
    time = request.args.get("time")
    prevention = request.args.get("prevention")
    if prevention == "1":
        return redirect("/city_1?time={}".format(time))
    else:
        return redirect("/city_1?time={}".format(time))


@app.route('/city_1')
def index_city_1():
    time = request.args.get("time")
    data = pd.read_csv(
        r"./static/data/4Number of disease prevention and control centers in China.csv")
    columns = data.columns.values
    data_x = data["地区"].values.tolist()
    data_y = data[time].values.tolist()

    province_distribution = {i: j for i, j in zip(data_x, data_y)}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())
    map = Map("中国疾病预防控制中心{}儿童死亡数量".format(time), '', width="50%")
    map.add("", provice, values, visual_range=[min(values), max(values)], maptype='china', is_visualmap=True,
            visual_text_color='#000')

    return render_template('index.html',
                           myechart=map.render_embed(),
                           script_list=map.get_js_dependencies(), text='''
                           疾病预防控制中心不仅是完成上级疾病预防控制任务的基层执行者，也有着指导基层医疗卫生机构完成疾病预防和控制具体工作的责任。而专科疾病防治院相比于一般的医院，有更强的针对性，面对不同疾病能提出更有效的治疗方案，在医疗水平不算发达的农村地区，专科疾病防治院往往能提供紧缺的“救命药”。
分析上述两个图标近10年来的数据，疾病预防控制中心在中东和北部地区有一定发展，但是其他地区总体趋于停滞；而专科疾病防治院在近10年发展趋于停滞，只在中部地区有较小发展，但是这两种机构对于降低中国5岁以下儿童乃至其他群体的死亡率有着非常重要的意义。
联系2018年中国5岁以下儿童主要死因分析数据，除去占比最高的“损伤和中毒”，“肿瘤”、“呼吸道疾病”、“传染类疾病”等疾病对儿童生命安全健康也有很大威胁。这些疾病中病发前的预防、病发时的控制以及病发后的针对性治疗，每一个环节都不掉链子才能真正守护儿童们的健康成长。而“诊断不明”在近10年儿童主要死因占比一直没有明显下降，这些都可以成为医疗救助的核心突破口。
因而，虽然许多地区的数据反映出病预防控制中心及专科疾病防治院已完成基本覆盖，能满足基本救援需求，但我国的发展已经迈入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾，而这两种医疗机构的发展停滞是不是就是不平衡不充分发展的一种体现呢？这值得我们思考，更值得我们努力。
                           ''', text1='''这次项目的数据采集主要围绕中国儿童死亡情况展开，搜集了近10年来中国5岁以下儿童（包含全体、城市、农村）死亡率数据、其主要死因的分析数据及可能存在的预防控制和专科救助情况数据。
总体来说我国5岁以下儿童死亡率在医疗水平提高以及国家专项纲要推动等因素下已经实现较大幅度的降低，但是农村儿童较高的死亡率仍然可以作为儿童生命安全健康任务的核心突破点。而对于儿童生存环境中存在的各种危险因素，人们的重视程度还是不够，要切实解决这些危险问题，首要做到的就是具体情况具体分析，切不可以以偏概全，对于家庭因素、地区因素、环境因素都要点对点提出宣传及解决建议。而针对疾病预防控制中心及专科疾病防治院的发展，最大问题是发展遇到瓶颈，被暂时性的饱和假象拖慢了发展脚步。儿童的疾病防治与专科诊疗问题从来不是“医疗机构基本覆盖”、“救援需求基本满足”可以解决，更充分的发展，更尖端技术的推广仍然任重道远。''')


@app.route('/city_2')
def index_city_2():
    time = request.args.get("time")
    data = pd.read_csv(
        r"./static/data/5Number of specialist disease prevention hospitals in China.csv")
    columns = data.columns.values
    data_x = data["地区"].values.tolist()
    data_y = data[time].values.tolist()

    province_distribution = {i: j for i, j in zip(data_x, data_y)}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())
    map = Map("中国专业疾病预防医院{}儿童死亡数量".format(time), '', width="50%")
    map.add("", provice, values, visual_range=[min(values), max(values)], maptype='china', is_visualmap=True,
            visual_text_color='#000')

    return render_template('index.html',
                           myechart=map.render_embed(),
                           script_list=map.get_js_dependencies(), text='''
                           疾病预防控制中心不仅是完成上级疾病预防控制任务的基层执行者，也有着指导基层医疗卫生机构完成疾病预防和控制具体工作的责任。而专科疾病防治院相比于一般的医院，有更强的针对性，面对不同疾病能提出更有效的治疗方案，在医疗水平不算发达的农村地区，专科疾病防治院往往能提供紧缺的“救命药”。
分析上述两个图标近10年来的数据，疾病预防控制中心在中东和北部地区有一定发展，但是其他地区总体趋于停滞；而专科疾病防治院在近10年发展趋于停滞，只在中部地区有较小发展，但是这两种机构对于降低中国5岁以下儿童乃至其他群体的死亡率有着非常重要的意义。
联系2018年中国5岁以下儿童主要死因分析数据，除去占比最高的“损伤和中毒”，“肿瘤”、“呼吸道疾病”、“传染类疾病”等疾病对儿童生命安全健康也有很大威胁。这些疾病中病发前的预防、病发时的控制以及病发后的针对性治疗，每一个环节都不掉链子才能真正守护儿童们的健康成长。而“诊断不明”在近10年儿童主要死因占比一直没有明显下降，这些都可以成为医疗救助的核心突破口。
因而，虽然许多地区的数据反映出病预防控制中心及专科疾病防治院已完成基本覆盖，能满足基本救援需求，但我国的发展已经迈入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾，而这两种医疗机构的发展停滞是不是就是不平衡不充分发展的一种体现呢？这值得我们思考，更值得我们努力。
                           ''', text1='''这次项目的数据采集主要围绕中国儿童死亡情况展开，搜集了近10年来中国5岁以下儿童（包含全体、城市、农村）死亡率数据、其主要死因的分析数据及可能存在的预防控制和专科救助情况数据。
总体来说我国5岁以下儿童死亡率在医疗水平提高以及国家专项纲要推动等因素下已经实现较大幅度的降低，但是农村儿童较高的死亡率仍然可以作为儿童生命安全健康任务的核心突破点。而对于儿童生存环境中存在的各种危险因素，人们的重视程度还是不够，要切实解决这些危险问题，首要做到的就是具体情况具体分析，切不可以以偏概全，对于家庭因素、地区因素、环境因素都要点对点提出宣传及解决建议。而针对疾病预防控制中心及专科疾病防治院的发展，最大问题是发展遇到瓶颈，被暂时性的饱和假象拖慢了发展脚步。儿童的疾病防治与专科诊疗问题从来不是“医疗机构基本覆盖”、“救援需求基本满足”可以解决，更充分的发展，更尖端技术的推广仍然任重道远。''')


if __name__ == '__main__':
    app.run(debug=True)
