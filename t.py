# rs = requests.get('https://cx.shouji.360.cn/phonearea.php?number=18942955144')
#
# d = rs.json().get('data')
# try:
#     place = d.get('province') + d.get('city')
# except AttributeError:
#     print("is None")
#
# print(d)
# print(place)
import requests

# rs = requests.get("https://config.net.cn/tools/ProvinceCityCountry.html")
# rs.encoding = rs.apparent_encoding
# t = rs.text
#
# city_dict = []
# soup = BeautifulSoup(t,'html.parser')
# tr = soup.select('tr')
# tr = tr[1:-1]
# for (i,t) in enumerate(tr):
#     td = t.select('td')
#     c_key = td[0].text
#     if city_dict.get(c_key) == None:
#         city_dict[c_key] = set((td[1].text,td[2].text))
#     else:
#         city_dict[c_key].add(td[1].text)
#         city_dict[c_key].add(td[2].text)
# print(city_dict)

city_data = {
    '北京市': ['西城区', '丰台区', '宣武区', '东城区', '石景山区', '门头沟区', '昌平区', '密云县', '崇文区', '延庆县',
               '朝阳区', '大兴区', '海淀区', '顺义区', '怀柔区', '房山区', '北京市', '通州区', '平谷区'],
    '天津市': ['西青区', '南开区', '河北区', '红桥区', '东丽区', '河东区', '大港区', '蓟县', '塘沽区', '津南区',
               '汉沽区', '静海县', '和平区', '宁河县', '宝坻区', '天津市', '河西区', '武清区', '北辰区'],
    '河北省': ['清苑县', '定州市', '辛集市', '新河县', '运河区', '文安县', '怀安县', '抚宁县', '青龙满族自治县',
               '迁西县', '行唐县', '巨鹿县', '泊头市', '饶阳县', '古冶区', '张北县', '山海关区', '临城县', '井陉县',
               '肥乡县', '涉县', '安新县', '东光县', '定兴县', '唐海县', '曲阳县', '安国市', '南皮县', '香河县',
               '路北区', '沧州市', '桥东区', '赞皇县', '新乐市', '南宫市', '涞水县', '卢龙县', '新市区', '衡水市',
               '广宗县', '海港区', '深州市', '邯郸县', '隆化县', '永年县', '蔚县', '井陉矿区', '张家口市', '武强县',
               '平泉县', '馆陶县', '吴桥县', '盐山县', '复兴区', '元氏县', '南和县', '沽源县', '任县', '清河县', '唐县',
               '故城县', '望都县', '景县', '任丘市', '滦南县', '永清县', '冀州市', '路南区', '邢台市', '长安区',
               '黄骅市', '开平区', '满城县', '保定市', '枣强县', '涞源县', '双桥区', '平乡县', '临西县', '涿鹿县',
               '高阳县', '武安市', '宣化区', '下花园区', '沧县', '阳原县', '滦县', '玉田县', '安平县', '高邑县', '新区',
               '赵县', '栾城县', '秦皇岛市', '博野县', '涿州市', '北市区', '大厂回族自治县', '昌黎县', '三河市',
               '宽城满族自治县', '霸州市', '成安县', '邢台县', '邱县', '鸡泽县', '鹰手营子矿区', '怀来县', '无极县',
               '新华区', '尚义县', '石家庄市', '孟村回族自治县', '桥西区', '宁晋县', '魏县', '蠡县', '唐山市',
               '峰峰矿区', '郊区', '威县', '康保县', '桃城区', '柏乡县', '海兴县', '承德市', '滦平县',
               '围场满族蒙古族自治县', '沙河市', '雄县', '晋州市', '大城县', '顺平县', '丰润县', '廊坊市', '磁县',
               '曲周县', '兴隆县', '武邑县', '万全县', '丛台区', '乐亭县', '鹿泉市', '南市区', '临漳县', '肃宁县',
               '崇礼县', '献县', '平山县', '内丘县', '承德县', '阜城县', '深泽县', '北戴河区', '邯山区', '青县',
               '隆尧县', '正定县', '藁城市', '丰宁满族自治县', '遵化市', '阜平县', '河间市', '易县', '广平县', '大名县',
               '双滦区', '邯郸市', '宣化县', '灵寿县', '徐水县', '固安县', '迁安市', '容城县', '赤城县', '丰南市',
               '安次区', '高碑店市'],
    '山西省': ['潞城市', '临汾市', '蒲县', '曲沃县', '怀仁县', '盂县', '和顺县', '平定县', '黎城县', '介休市', '南郊区',
               '兴县', '武乡县', '平遥县', '右玉县', '方山县', '交城县', '忻府区', '阳曲县', '左权县', '安泽县', '应县',
               '古县', '杏花岭区', '洪洞县', '左云县', '清徐县', '绛县', '陵川县', '太谷县', '阳泉市', '孝义市',
               '平陆县', '永和县', '平顺县', '原平市', '柳林县', '沁水县', '娄烦县', '昔阳县', '长子县', '临县',
               '平鲁区', '保德县', '浮山县', '城区', '榆社县', '文水县', '广灵县', '运城市', '代县', '隰县', '襄垣县',
               '繁峙县', '乡宁县', '尖草坪区', '太原市', '吉县', '霍州市', '迎泽区', '宁武县', '离石区', '五寨县',
               '岚县', '灵石县', '沁源县', '夏县', '朔州市', '阳城县', '定襄县', '新荣区', '神池县', '侯马市', '长治市',
               '寿阳县', '大同县', '沁县', '垣曲县', '壶关县', '万柏林区', '灵丘县', '高平市', '忻州市', '汾阳市',
               '大宁县', '阳高县', '稷山县', '古交市', '万荣县', '永济市', '山阴县', '榆次市', '新绛县', '中阳县',
               '交口县', '郊区', '浑源县', '翼城县', '晋源区', '泽州县', '芮城县', '襄汾县', '晋中市', '岢岚县',
               '晋城市', '静乐县', '吕梁市', '矿区', '临猗县', '石楼县', '偏关县', '汾西县', '天镇县', '河曲县',
               '大同市', '长治县', '闻喜县', '小店区', '朔城区', '五台县', '河津市', '祁县', '屯留县'],
    '内蒙古': ['扎兰屯市', '锡林郭勒盟', '霍林郭勒市', '阿拉善盟', '喀喇沁旗', '满洲里市', '镶黄旗', '阿拉善左旗',
               '化德县', '集宁市', '海勃湾区', '库伦旗', '五原县', '准格尔旗', '鄂托克旗', '包头市', '锡林浩特市',
               '新巴尔虎右旗', '阿巴嘎旗', '卓资县', '乌拉特后旗', '东河区', '额尔古纳市', '清水河县', '敖汉旗',
               '扎鲁特旗', '察哈尔右翼后旗', '阿尔山市', '牙克石市', '临河市', '正镶白旗', '呼和浩特市', '武川县',
               '多伦县', '根河市', '莫力达瓦达斡尔族自治旗', '东乌珠穆沁旗', '巴林右旗', '松山区', '商都县',
               '二连浩特市', '科尔沁右翼中旗', '赤峰市', '海南区', '扎赉特旗', '四子王旗', '乌兰浩特市', '苏尼特左旗',
               '固阳县', '林西县', '乌审旗', '达尔罕茂明安联合旗', '宁城县', '鄂温克族自治旗', '突泉县', '乌兰察布盟',
               '玉泉区', '红山区', '翁牛特旗', '乌拉特前旗', '苏尼特右旗', '元宝山区', '和林格尔县', '土默特左旗',
               '兴和县', '开鲁县', '伊克昭盟（鄂尔多斯旧称）', '海拉尔市', '阿拉善右旗', '托克托县', '白云矿区', '杭锦旗',
               '磴口县', '科尔沁左翼中旗', '石拐矿区', '克什克腾旗', '科尔沁左翼后旗', '阿荣旗', '阿鲁科尔沁旗', '郊区',
               '额济纳旗', '察哈尔右翼中旗', '东胜市', '达拉特旗', '凉城县', '土默特右旗', '回民区', '通辽市',
               '巴林左旗', '科尔沁右翼前旗', '伊金霍洛旗', '科尔沁区', '青山区', '察哈尔右翼前旗', '巴彦淖尔盟',
               '呼伦贝尔市', '太仆寺旗', '新城区', '乌海市', '西乌珠穆沁旗', '新巴尔虎左旗', '丰镇市', '乌拉特中旗',
               '奈曼旗', '鄂伦春自治旗', '兴安盟', '陈巴尔虎旗', '正蓝旗', '鄂托克前旗', '乌达区', '杭锦后旗',
               '昆都伦区'],
    '辽宁省': ['瓦房店市', '大东区', '清河门区', '大洼县', '露天区', '元宝区', '新宾满族自治县', '古塔区', '彰武县',
               '白塔区', '明山区', '盖州市', '凌源市', '文圣区', '营口市', '千山区', '建昌县', '南票区', '和平区',
               '北票市', '庄河市', '凌河区', '站前区', '岫岩满族自治县', '双台子区', '铁法市', '喀喇沁左翼蒙古族自治县',
               '凤城市', '兴隆台区', '宏伟区', '铁西区', '抚顺县', '海州区', '辽中县', '清河区', '海城市', '朝阳市',
               '铁岭县', '平山区', '朝阳县', '建平县', '中山区', '银州区', '振安区', '双塔区', '太平区', '新抚区',
               '沈阳市', '铁东区', '连山区', '新邱区', '望花区', '龙城区', '太和区', '义县', '大石桥市', '康平县',
               '昌图县', '本溪市', '宽甸满族自治县', '法库县', '甘井子区', '龙港区', '盘锦市', '金州区', '辽阳县',
               '老边区', '灯塔市', '苏家屯区', '铁岭市', '立山区', '开原市', '细河区', '阜新蒙古族自治县', '沈河区',
               '西市区', '台安县', '绥中县', '西丰县', '锦州市', '鲅鱼圈区', '阜新市', '东港市', '黑山县', '南芬区',
               '桓仁满族自治县', '弓长岭区', '长海县', '辽阳市', '鞍山市', '于洪区', '葫芦岛市', '本溪满族自治县',
               '沙河口区', '旅顺口区', '溪湖区', '顺城区', '新城子区', '新民市', '丹东市', '东陵区', '西岗区',
               '清原满族自治县', '大连市', '凌海市', '北宁市', '太子河区', '抚顺市', '普兰店市', '振兴区', '兴城市',
               '盘山县', '皇姑区'],
    '吉林省': ['二道区', '八道江区', '铁西区', '西安区', '临江市', '德惠市', '集安市', '四平市', '梨树县', '江源县',
               '镇赉县', '昌邑区', '大安市', '长岭县', '双辽市', '抚松县', '宁江区', '二道江区', '白山市', '安图县',
               '长春市', '农安县', '南关区', '九台市', '辽源市', '敦化市', '延吉市', '汪清县', '双阳区', '龙井市',
               '扶余县', '吉林市', '通化市', '朝阳区', '东丰县', '伊通满族自治县', '磐石市', '和龙市', '梅河口市',
               '船营区', '龙潭区', '舒兰市', '桦甸市', '乾安县', '铁东区', '白城市', '龙山区', '永吉县', '靖宇县',
               '延边朝鲜族自治州', '图们市', '通榆县', '长白朝鲜族自治县', '公主岭市', '柳河县', '榆树市', '东昌区',
               '辉南县', '前郭尔罗斯蒙古族自治县', '东辽县', '通化县', '丰满区', '宽城区', '绿园区', '松原市', '洮北区',
               '洮南市', '珲春市', '蛟河市'],
    '黑龙江省': ['富拉尔基区', '林甸县', '龙沙区', '同江市', '肇州县', '通河县', '东安区', '七台河市', '大同区',
                 '依安县', '青冈县', '黑河市', '松北区', '延寿县', '牡丹江市', '庆安县', '南岗区', '兰西县', '泰来县',
                 '海伦市', '富锦市', '呼玛县', '美溪区', '塔河县', '嘉荫县', '带岭区', '孙吴县', '尖山区', '昂昂溪区',
                 '建华区', '宾县', '抚远县', '饶河县', '茄子河区', '木兰县', '四方台区', '鸡东县', '齐齐哈尔市',
                 '依兰县', '富裕县', '龙凤区', '乌马河区', '阳明区', '宝山区', '西林区', '东风区', '麻山区', '宁安市',
                 '岭东区', '萨尔图区', '克东县', '密山市', '漠河县', '巴彦县', '新兴区', '恒山区', '讷河市', '道外区',
                 '阿成区', '伊春区', '尚志市', '城子河区', '桦南县', '勃利县', '东宁县', '桃山区', '宝清县', '新青区',
                 '梅里斯达斡尔族区', '鸡西市', '向阳区', '前进区', '五常市', '工农区', '梨树区', '友谊县', '萝北县',
                 '五营区', '兴安区', '上甘岭区', '绥化市', '大兴安岭地区', '安达市', '哈尔滨市', '翠峦区', '龙江县',
                 '绥棱县', '肇源县', '桦川县', '鸡冠区', '伊春市', '郊区', '双鸭山市', '甘南县', '克山县', '道里区',
                 '绥滨县', '集贤县', '爱民区', '西安区', '兴山区', '让胡路区', '呼兰区', '南岔区',
                 '杜尔伯特蒙古族自治县', '逊克县', '汤原县', '大庆市', '碾子山区', '东山区', '南山区', '滴道区',
                 '绥芬河市', '铁锋区', '爱辉区', '五大连池市', '平房区', '乌伊岭区', '肇东市', '明水县', '虎林市',
                 '穆棱市', '林口县', '北安市', '望奎县', '香坊区', '红岗区', '友好区', '金山屯区', '方正县', '海林市',
                 '嫩江县', '双城市', '铁力市', '汤旺河区', '红星区', '拜泉县', '鹤岗市'],
    '上海市': ['虹口区', '徐汇区', '宝山区', '卢湾区', '闸北区', '黄浦区', '长宁区', '崇明县', '青浦区', '南汇区',
               '浦东新区', '金山区', '静安区', '嘉定区', '松江区', '杨浦区', '奉贤区', '闵行区', '普陀区', '上海市'],
    '江苏省': ['金湖县', '北塘区', '京口区', '宿迁市', '常州市', '滨海县', '高港区', '平江区', '张家港市', '邳州市',
               '泗阳县', '徐州市', '连云区', '大丰市', '高淳县', '姜堰市', '吴江市', '淮安市', '东台市', '江阴市',
               '启东市', '宝应县', '崇安区', '云龙区', '南长区', '马山区', '锡山市', '铜山县', '涟水县', '海州区',
               '沭阳县', '金坛市', '射阳县', '昆山市', '洪泽县', '清河区', '鼓楼区', '金阊区', '城区', '如皋市',
               '贾汪区', '清浦区', '泰兴市', '润州区', '吴县市', '海门市', '广陵区', '海陵区', '灌云县', '江宁区',
               '兴化市', '浦口区', '钟楼区', '扬中市', '沛县', '沧浪区', '南通市', '建邺区', '扬州市', '宿城区',
               '通州市', '阜宁县', '江都市', '白下区', '秦淮区', '句容市', '港闸区', '栖霞区', '六合区', '建湖县',
               '无锡市', '丹阳市', '新沂市', '睢宁县', '仪征市', '连云港市', '云台区', '丰县', '武进市', '海安县',
               '下关区', '郊区', '常熟市', '苏州市', '赣榆县', '九里区', '如东县', '宜兴市', '盱眙县', '东海县',
               '靖江市', '高邮市', '崇川区', '南京市', '泉山区', '淮阴县', '泗洪县', '泰州市', '盐都县', '新浦区',
               '天宁区', '太仓市', '宿豫县', '丹徒县', '盐城市', '邗江县', '镇江市', '戚墅堰区', '灌南县', '溧阳市',
               '溧水县', '玄武区', '雨花台区', '响水县', '淮安市(原淮阴市）'],
    '浙江省': ['秀城区', '舟山市', '拱墅区', '西湖区', '黄岩区', '瑞安市', '宁波市', '桐乡市', '庆元县', '新昌县',
               '缙云县', '平阳县', '金华市', '江山市', '滨江区', '平湖市', '青田县', '镇海区', '海盐县', '海宁市',
               '温岭市', '慈溪市', '洞头县', '嘉善县', '下城区', '常山县', '玉环县', '龙泉市', '临海市', '温州市',
               '海曙区', '磐安县', '湖州市', '金华县', '文成县', '衢县', '淳安县', '绍兴市', '武义县', '龙游县',
               '江北区', '江东区', '松阳县', '东阳市', '诸暨市', '婺城区', '鹿城区', '永嘉县', '天台县', '上城区',
               '越城区', '苍南县', '泰顺县', '定海区', '嘉兴市', '衢州市', '郊区', '路桥区', '乐清市', '北仑区',
               '台州市', '浦江县', '普陀区', '富阳市', '建德市', '绍兴县', '德清县', '义乌市', '三门县', '云和县',
               '兰溪市', '龙湾区', '象山县', '嵊泗县', '景宁畲族自治县', '仙居县', '余姚市', '丽水市', '南浔区',
               '萧山市', '杭州市', '椒江区', '余杭市', '宁海县', '遂昌县', '岱山县', '嵊州市', '江干区', '鄞县',
               '长兴县', '瓯海区', '安吉县', '永康市', '奉化市', '上虞市', '桐庐县', '开化县', '柯城区', '吴兴区',
               '临安市'],
    '安徽省': ['滁州市', '金家庄区', '宁国市', '临泉县', '杜集区', '巢湖区', '阜南县', '濉溪县', '巢湖市', '广德县',
               '迎江区', '东市区', '望江县', '淮南市', '全椒县', '萧县', '金安区', '琅琊区', '东至县', '霍山县',
               '枞阳县', '田家庵区', '铜陵县', '徽州区', '雨山区', '鸠江区', '绩溪县', '相山区', '芜湖市', '南谯区',
               '凤台县', '怀远县', '芜湖县', '宣州区', '铜官山区', '含山县', '裕安区', '镜湖区', '宿州市', '屯溪区',
               '颍泉区', '太湖县', '天长市', '池州市', '桐城市', '泗县', '新芜区', '安庆市', '大通区', '谢家集区',
               '明光市', '狮子山区', '烈山区', '宿松县', '岳西县', '长丰县', '马鞍山市', '阜阳市', '怀宁县', '八公山区',
               '祁门县', '潘集区', '黄山区', '南陵县', '庐江县', ' 墉桥区', '和县', '大观区', '潜山县', '肥东县',
               '西市区', '郊区', '蚌埠市', '旌德县', '舒城县', '马塘区', '郎溪县', '贵池区', '颍州区', '泾县', '灵璧县',
               '宣城市', '铜陵市', '黄山市', '太和县', '当涂县', '歙县', '颍上县', '青阳县', '淮北市', '五河县',
               '肥西县', '来安县', '合肥市', '固镇县', '寿县', '砀山县', '颍东区', '金寨县', '霍邱县', '石台县',
               '繁昌县', '六安市', '中市区', '花山区', '黟县', '无为县', '定远县', '凤阳县', '界首市', '休宁县'],
    '福建省': ['永泰县', '尤溪县', '晋安区', '洛江区', '泰宁县', '台江区', '连城县', '诏安县', '涵江区', '华安县',
               '上杭县', '福州市', '屏南县', '长泰县', '建阳市', '永定县', '漳州市', '邵武市', '云霄县', '闽侯县',
               '将乐县', '福安市', '三明市', '平和县', '武平县', '鲤城区', '南安市', '秀屿区', '延平区', '东山县',
               '泉港区', '建瓯市', '长汀县', '连江县', '龙岩', '龙海市', '鼓楼区', '永安市', '平潭县', '浦城县',
               '罗源县', '集美区', '城厢区', '闽清县', '晋江市', '寿宁县', '莆田市', '松溪县', '石狮市', '周宁县',
               '德化县', '政和县', '海沧区', '三元区', '光泽县', '湖里区', '福清市', '金门县', '丰泽区', '芗城区',
               '梅列区', '仓山区', '大田县', '永春县', '霞浦县', '明溪县', '南平市', '武夷山市', '蕉城区', '宁德市',
               '古田县', '新罗区', '南靖县', '同安区', '长乐市', '安溪县', '漳平市', '惠安县', '建宁县', '宁化县',
               '荔城区', '龙文区', '清流县', '马尾区', '沙\u3000县', '思明区?', '厦门市', '漳浦县', '柘荣县', '翔安区',
               '顺昌县', '福鼎市', '泉州市', '仙游县'],
    '江西省': ['贵溪市', '寻乌县', '横峰县', '西湖区', '永新县', '抚州市', '金溪县', '余江县', '波阳县', '湾里区',
               '珠山区', '德兴市', '樟树市', '崇仁县', '婺源县', '铜鼓县', '兴国县', '奉新县', '大余县', '月湖区',
               '南昌市', '宁冈县', '宜丰县', '浔阳区', '渝水区', '分宜县', '芦溪县', '九江县', '上犹县', '浮梁县',
               '莲花县', '靖安县', '湘东区', '弋阳县', '青云谱区', '南康市', '上饶县', '新建县', '东湖区', '万载县',
               '乐平市', '永修县', '宜黄县', '进贤县', '信丰县', '广丰县', '南丰县', '吉安县', '上高县', '上饶市',
               '安义县', '临川市', '九江市', '赣州市', '遂川县', '全南县', '新余市', '广昌县', '石城县', '瑞金市',
               '安源区', '永丰县', '余干县', '会昌县', '昌江区', '丰城市', '龙南县', '赣县', '峡江县', '万年县',
               '彭泽县', '南昌县', '章贡区', '东乡县', '安远县', '德安县', '郊区', '于都县', '星子县', '乐安县',
               '庐山区', '铅山县', '高安市', '吉安市', '瑞昌市', '萍乡市', '上栗县', '玉山县', '井冈山市', '新干县',
               '资溪县', '宁都县', '崇义县', '万安县', '景德镇市', '吉水县', '安福县', '泰和县', '南城县', '鹰潭市',
               '宜春市', '都昌县', '湖口县', '黎川县', '武宁县', '修水县', '定南县'],
    '山东省': ['莱州市', '泰山区', '冠县', '胶州市', '莱西市', '蓬莱市', '东明县', '奎文区', '兰山区', '宁阳县',
               '李沧区', '金乡县', '乳山市', '河东区', '牟平区', '海阳市', '安丘市', '枣庄市', '东阿县', '东平县',
               '山亭区', '莒南县', '滨州地区', '齐河县', '滨州市', '坊子区', '新泰市', '兖州市', '潍城区', '任城区',
               '槐荫区', '五莲县', '临清市', '莘县', '东昌府区', '昌邑市', '黄岛区', '荣成市', '东营区', '岚山区',
               '郓城县', '梁山县', '微山县', '寿光市', '陵县', '武城县', '阳信县', '长清县', '宁津县', '东营市',
               '临朐县', '龙口市', '博兴县', '济南市', '张店区', '菏泽地区', '平阴县', '郯城县', '青岛市', '环翠区',
               '高密市', '禹城市', '寒亭区', '高唐县', '嘉祥县', '夏津县', '邹平县', '临沂市', '临淄区', '芝罘区',
               '薛城区', '文登市', '章丘市', '莱城区', '日照市', '鄄城县', '蒙阴县', '市北区', '平原县', '峄城区',
               '淄博市', '德城区', '城阳区', '历城区', '惠民县', '淄川区', '东港区', '阳谷县', '青州市', '莒县',
               '桓台县', '博山区', '菏泽市', '滕州市', '胶南市', '垦利县', '昌乐县', '平度市', '高青县', '沂源县',
               '茌平县', '河口区', '沂水县', '济宁市', '莱山区', '汶上县', '罗庄区', '平邑县', '郊区', '四方区',
               '巨野县', '利津县', '崂山区', '乐陵市', '成武县', '莱阳市', '福山区', '费县', '聊城市', '即墨市',
               '烟台市', '曲阜市', '莱芜市', '台儿庄区', '曹县', '定陶县', '肥城市', '长岛县', '市南区', '德州市',
               '天桥区', '广饶县', '泗水县', '单县', '庆云县', '泰安市', '沾化县', '诸城市', '商河县', '无棣县',
               '栖霞市', '沂南县', '历下区', '临邑县', '鱼台县', '济阳县', '招远市', '临沭县', '周村区', '邹城市',
               '威海市', '潍坊市', '钢城区', '苍山县', '市中区'],
    '河南省': ['焦作市', '伊川县', '林州市', '孟州市', '通许县', '鹤山区', '修武县', '许昌县', '漯河市', '鹿邑县',
               '驻马店地区', '文峰区', '驻马店市', '省直辖行政单位', '夏邑县', '淮阳县', '开封县', '桐柏县', '固始县',
               '上蔡县', '清丰县', '栾川县', '滑县', '睢阳区', '辉县市', '宛城区', '沈丘县', '宁陵县', '淇县', '扶沟县',
               '延津县', '台前县', '信阳市', '涧西区', '红旗区', '汤阴县', '获嘉县', '新乡市', '解放区', '梁园区',
               '吉利区', '石龙区', '洛宁县', '管城回族区', '罗山县', '陕县', '博爱县', '铁西区', '北站区', '山城区',
               '原阳县', '确山县', '卢氏县', '鼓楼区', '宜阳县', '汝南县', '渑池县', '金水区', '宝丰县', '平舆县',
               '魏都区', '禹州市', '老城区', '淮滨县', '襄城县', '新郑市', '尉氏县', '新野县', '中牟县', '鹤壁市',
               '新密市', '郸城县', '淅川县', '西工区', '山阳区', '潢川县', '召陵区', '息县', '西华县', '柘城县',
               '正阳县', '温县', '方城县', '长垣县', '卧龙区', '济源市', '平顶山市', '沁阳市', '廛河回族区', '许昌市',
               '新乡县', '封丘县', '灵宝市', '睢县', '舞阳县', '顺河回族区', '商丘市', '商水县', '西峡县', '卫东区',
               '二七区', '巩义市', '卫辉市', '汝州市', '龙亭区', '永城市', '太康县', '新华区', '马村区', '华龙区',
               '开封市', '社旗县', '邓州市', '洛阳市', '舞钢市', '嵩县', '郊区', '中站区', '长葛市', '偃师市', '唐河县',
               '郏县', '南召县', '内黄县', '郾城区', '民权县', '濮阳县', '鄢陵县', '遂平县', '安阳市', '安阳县',
               '新安县', '虞城县', '南阳市', '\uf8f2负忧\uf8f8', '项城市', '鲁山县', '新县', '临颍县', '三门峡市',
               '西平县', '南关区', '郑州市', '濮阳市', '湛河区', '中原区', '上街区', '南乐县', '源汇区', '杞县',
               '平桥区', '镇平县', '武陟县', '浚县', '义马市', '商城县', '兰考县', '叶县', '湖滨区', '荥阳市', '北关区',
               '范县', '光山县', '周口市', '邙山区', '汝阳县', '登封市', '泌阳县', '新蔡县', '内乡县', '孟津县'],
    '湖北省': ['来凤县', '郧县', '随县', '曾都区', '省直辖行政单位', '黄州区', '黄陂区', '公安县', '远安县', '广水市',
               '掇刀区', '咸丰县', '石首市', '新洲区', '利川市', '武穴市', '兴山县', '大悟县', '通城县', '丹江口市',
               '麻城市', '钟祥市', '江汉区', '孝南区', '乔口区', '荆州市', '云梦县', '大冶市', '五峰土家族自治县',
               '崇阳县', '赤壁市', '浠水县', '江岸区', '红安县', '当阳市', '襄城区', '襄阳市', '南漳县', '梁子湖区',
               '松滋市', '长阳土家族自治县', '汉阳区', '咸宁市', '石灰窑区', '枣阳市', '洪湖市', '建始县', '华容区',
               '嘉鱼县', '应城市', '黄梅县', '恩施市', '孝感市', '竹溪县', '荆州区', '老河口市', '鹤峰县', '铁山区',
               '宣恩县', '虎亭区', '宜昌县', '宜都市', '随州市', '宜昌市', '茅箭区', '团风县', '郧西县', '巴东县',
               '张湾区', '京山县', '蕲春县', '西陵区', '宜城市', '保康县', '伍家岗区', '罗田县', '天门市', '枝江市',
               '武汉市', '神农架林区', '荆门市', '仙桃市', '竹山县', '安陆市', '点军区', '秭归县', '监利县', ' 咸安区',
               '黄石港区', '东西湖区', '房县', '蔡甸区', '鄂城区', '阳新县', '十堰市', '通山县', '下陆区', '青山区',
               '汉南区', '黄石市', '谷城县', '江陵县', '汉川市', '沙市区', '黄冈市', '洪山区', '东宝区', '孝昌县',
               '恩施土家族苗族自治州', '沙洋县', '鄂州市', '樊城区', '襄樊市', '襄阳县', '潜江市', '武昌区', '江夏区',
               '英山县'],
    '湖南省': ['麻阳苗族自治县', '长沙县', '岳阳楼区', '湘西土家族苗族自治州', '武陵源区', '赫山区', '衡东县', '郊 区',
               '临湘市', '溆浦县', '永兴县', '娄底地区', '北湖区', '芙蓉区', '双峰县', '东安县', '雨花区', '临澧县',
               '桂东县', '安化县', '湘阴县', '岳麓区', '江华瑶族自治县', '醴陵市', '平江县', '耒阳市', '汉寿县',
               '新宁县', '君山区', '资兴市', '南县', '天心区', '炎陵县', '湘乡市', '岳塘区', '城南区', '天元区',
               '北塔区', '辰溪县', '嘉禾县', '衡阳县', '新化县', '花垣县', '双牌县', '怀化市', '常德市', '冷水滩区',
               '桂阳县', '江永县', '岳阳市', '新邵县', '鹤城区', '芝山区', '祁阳县', '韶山市', '常宁市',
               '芷江侗族自治县', '中方县', '武冈市', '云溪区', '通道侗族自治县', '衡南县', '道县', '岳阳县', '娄底市',
               '冷水江市', '开福区', '凤凰县', '永州市', '宜章县', '浏阳市', '大祥区', '南岳区', '古丈县', '洞口县',
               '泸溪县', '邵东县', '宁乡县', '江东区', '慈利县', '安仁县', '城步苗族自治县', '张家界市', '石门县',
               '城北区', '茶陵县', '隆回县', '雨湖区', '芦淞区', '临武县', '津市市', '株洲县', '永顺县', '桑植县',
               '汝城县', '新田县', '吉首市', '石峰区', '衡阳市', '保靖县', '益阳市', '衡山县', '洪江市', '邵阳县',
               '永定区', '祁东县', '桃源县', '资阳区', '双清区', '靖州苗族侗族自治县', '汨罗市', '沅江市', '鼎城区',
               '新晃侗族自治县', '华容县', '涟源市', '绥宁县', '湘潭市', '沅陵县', '望城县', '安乡县', '武陵区',
               '株洲市', '荷塘区', '龙山县', '桃江县', '长沙市', '湘潭县', '邵阳市', '攸县', '澧县', '苏仙区', '宁远县',
               '蓝山县', '郴州市', '会同县'],
    '广东省': ['云浮市', '高明区', '揭西县', '龙川县', '浈江区', '东城区', '揭东县', '南城区', '始兴县', '罗湖区',
               '阳山县', '清新县', '江门市', '兴宁市', '廉江市', '龙湖区', '仁化县', '从化市', '罗定市', '五华县',
               '信宜市', '普宁市', '潮阳区', '茂南区', '阳东县', '东莞市', '宝安区', '韶关市', '英德市',
               '连南瑶族自治县', '中山市', '曲江区', '霞山区', '蓬江区', '龙门县', '海珠区', '天河区', '高要市',
               '丰顺县', '河源市', '赤坎区', '佛冈县', '陆河县', '湘桥区', '鹤山市', '开平市', '黄埔区', '白云区',
               '汕头市', '肇庆市', '封开县', '莞城区', '蕉岭县', '遂溪县', '荔湾区', '广州市', '龙岗区', '城区',
               '珠海市', '南海区', '连州市', '惠阳市', '阳江市', '海丰县', '紫金县', '南澳县', '高州市', '化州市',
               '清城区', '越秀区', '乐昌市', '广宁县', '东源县', '深圳市', '端州区', '梅江区', '惠城区', '大埔县',
               '潮安县', '鼎湖区', '斗门区', '茂名市', '顺德区', '电白县', '盐田区', '连山壮族瑶族自治县', '阳春市',
               '怀集县', '濠江区', '麻章区', '江城区', '香洲区', '陆丰市', '榕城区', '潮南区', '禅城区', '佛山市',
               '恩平市', '源城区', '梅州市', '新丰县', '万江区', '吴川市', '福田区', '茂港区', '和平县', '揭阳市',
               '云城区', '三水区', '番禺市', '饶平县', '博罗县', '增城市', '翁源县', '武江区', '梅县', '清远市',
               '云安县', '台山市', '东山区', '江海区', '南山区', '平远县', '金湾区', '金平区', '花都市', '南雄市',
               '新兴县', '澄海区', '潮州市', '汕尾市', '惠来县', '乳源瑶族自治县', '湛江市', '新会市', '德庆县',
               '徐闻县', '阳西县', '郁南县', '惠州市', '连平县', '四会市', '雷州市', '惠东县', '坡头区', '芳村区'],
    '广西省': ['柳江县', '江南区', '上思县', '城中区', '荔蒲县', '兴安县', '贵港市', '罗城仫佬族自治县', '西乡塘区',
               '灵山县', '金城江区', '凭祥市', '钟山县', '武鸣县', '铁山港区', '港口区', '临桂县', '凌云县', '银海区',
               '昭平县', '钦北区', '永福县', '忻城县', '柳北区', '大化瑶族自治县', '兴业县', '雁山区', '百色市',
               '钦南区', '平南县', '柳南区', '灌阳县', '兴宁区', '右江区', '东兰县', '桂平市', '覃塘区', '玉州区',
               '扶绥县', '天峨县', '邕宁区', '岑溪市', '河池市', '马山县', '良庆区', '田东县', '南丹县', '浦北县',
               '崇左市', '隆林各族自治县', '博白县', '都安瑶族自治县', '市郊区', '田阳县', '宾阳县', '港北区',
               '金秀瑶族自治县', '玉林市', '柳州市', '象州县', '靖西县', '恭城瑶族自治县', '全州县', '上林县', '平乐县',
               '龙胜各县自治区', '桂林市', '来宾市', '海城区', '龙州县', '德保县', '青秀区', '宜州市', '八步区',
               '环江毛南族自治县', '巴马瑶族自治县', '合浦县', '南宁市', '防城区', '融安县', '乐业县', '鹿寨县',
               '江州区', '防城港市', '三江侗族自治县', '横\u3000县', '武宣县', '大新县', '柳城县', '阳朔县', '象山区',
               '蒙山县', '钦州市', '富川瑶族自治县', '田林县', '叠彩区', '贺州市', '平果县', '灵川县', '北海市',
               '七星区', '合山市', '鱼峰区', '苍梧县', '东兴市', '万秀区', '兴宾区', '宁明县', '梧州市', '凤山县',
               '容县', '资源县', '西林县', '隆安县', '秀峰区', '港南区', '陆川县', '藤县', '北流市', '蝶山区', '天等县',
               '那坡县', '融水苗族自治县'],
    '海南省': ['龙华区', '五指山市', '定安县', '海口市', '琼中黎族苗族自治县', '省直辖行政单位', '陵水黎族自治县',
               '白沙黎族自治县', '澄迈县', '美兰区', '乐东黎族自治县', '临高县', '文昌市', '秀英区', '万宁市', '东方市',
               '三亚市', '昌江黎族自治县', '琼山区', '市辖区', '保亭黎族苗族自治县', '琼海市', '儋州市',
               '西南中沙群岛办事处', '屯昌县'],
    '重庆市': ['璧山县', '巫溪县', '酉阳土家族苗族自治县', '巴南区', '荣昌县', '江津市', '万州区', '沙坪坝区', '梁平县',
               '渝中区', '渝北区', '永川市', '合川市', '忠县', '石柱土家族自治县', '巫山县', '潼南县', '涪陵区',
               '北碚区', '江北区', '重庆市', '铜梁县', '武隆县', '开县', '万盛区', '大足县', '秀山土家族苗族自治县',
               '长寿县', '云阳县', '垫江县', '大渡口区', '奉节县', '九龙坡区', '南岸区', '彭水苗族土家族自治县',
               '綦江县', '丰都县', '南川市', '城口县', '双桥区', '黔江土家族苗族自治县'],
    '四川省': ['甘孜藏族自治州', '都江堰市', '营山县', '屏山县', '青神县', '罗江县', '南充市', '金阳县', '彭州市',
               '阿坝藏族羌族自治州', '资阳地区', '凉山彝族自治州', '安岳县', '成华区', '米易县', '长宁县', '道孚县',
               '金堂县', '高坪区', '资中县', '仁寿县', '武侯区', '仁和区', '兴文县', '名山县', '自流井区', '稻城县',
               '威远县', '利州区', '盐亭县', '犍为县', '锦江区', '三台县', '康定县', '乡城县', '龙泉驿区', '游仙区',
               '甘洛县', '古蔺县', '南部县', '冕宁县', '双流县', '高县', '沙湾区', '达川市', '德阳市', '顺庆区',
               '阆中市', '南溪县', '元坝区', '贡井区', '五通桥区', '巴中地区', '巴中市', '金川县', '安县', '渠县',
               '旺苍县', '汶川县', '南江县', '沐川县', '新都县', '剑阁县', '江油市', '龙马潭区', '遂宁市', '炉霍县',
               '什邡市', '平昌县', '成都市', '达川地区', '筠连县', '新津县', '宁南县', '眉山地区', '阿坝县', '嘉陵区',
               '德格县', '崇州市', '广安市', '色达县', '绵竹市', '理县', '普格县', '壤塘县', ' 邻水县', '松潘县',
               '合江县', '青白江区', '纳溪区', '若尔盖县', '喜德县', '雅安市', '美姑县', '叙永县', '珙县', '天全县',
               '大邑县', '宣汉县', '江阳区', '泸县', '大英县', '荥经县', '青川县', '翠屏区', '汉源县', '东兴区',
               '新龙县', '温江县', '雷波县', '通江县', '攀枝花市', '会理县', '金牛区', '红原县', '峨边彝族自治县',
               '\u3000安居区', '得荣县', '小金县', '峨眉山市', '大竹县', '白玉县', '中江县', '平武县', '北川县',
               '邛崃市', '万源市', '雅安地区', '马尔康县', '宝兴县', '江安县', '理塘县', '巴塘县', '简阳市', '大安区',
               '绵阳市', '金口河区', '彭山县', '夹江县', ' 武胜县', '梓潼县', '苍溪县', '乐至县', '昭觉县', '荣县',
               '泸定县', '蓬安县', '涪城区', '隆昌县', '青羊区', '自贡市', '郫县', '马边彝族自治县', '宜宾县',
               ' 华莹市', '黑水县', '甘孜县', '旌阳区', '内江市', '沿滩区', '仪陇县', '九寨沟县', '广安区', '德昌县',
               '宜宾市', '蒲江县', '西区', '富顺县', '越西县', '木里藏族自治县', '船山区', '广元市', '石棉县', '盐边县',
               '井研县', ' 岳池县', '射洪县', '西昌市', '茂县', '眉山县', '蓬溪县', '东区', '石渠县', '雅江县',
               '乐山市', '九龙县', '芦山县', '广汉市', '盐源县', '布拖县', '开江县', '达县', '泸州市', '洪雅县',
               '丹巴县', '资阳市', '西充县', '会东县', '朝天区', '丹棱县', '市中区'],
    '贵州省': ['云岩区', '威宁彝族回族苗族自治县', '六枝特区', '赤水市', '金沙县', '镇远县', '南明区',
               '黔南布依族苗族自治州', '册亨县', '正安县', '剑河县', '思南县', '锦屏县', '息烽县', '铜仁地区',
               '黔西南布依族苗族自治州', '石阡县', '凯里市', '湄潭县', '安顺市', '钟山区', '天柱县', '普安县', '兴仁县',
               '赫章县', '白云区', '开阳县', '丹寨县', '铜仁市', '普定县', '施秉县', '三都水族自治县', '罗甸县',
               '瓮安县', '惠水县', '独山县', '万山特区', '遵义县', '兴义市', '道真仡佬族苗族自治县',
               '务川仡佬族苗族自治县', '福泉市', '沿河土家族自治县', '紫云苗族布依族自治县', '岑巩县', '荔波县',
               '绥阳县', '六盘水市', '德江县', '龙里县', '水城县', '桐梓县', '红花岗区', '安顺地区', '汇川区', '清镇市',
               '习水县', '从江县', '毕节地区', '晴隆县', '遵义市', '纳雍县', '仁怀市', '望谟县', '花溪区', '毕节市',
               '贵定县', '修文县', '黄平县', '雷山县', '余庆县', '乌当区', '麻江县', '松桃苗族自治县', '织金县',
               '黔西县', '盘县特区', '凤冈县', '安龙县', '镇宁布依族苗族自治县', '平坝县', '贵阳市', '都匀市', '平塘县',
               '三穗县', '江口县', '黎平县', '大方县', '小河区', '黔东南苗族侗族自治州', '榕江县', '贞丰县',
               '印江土家族苗族自治县', '玉屏侗族自治县', '长顺县', '关岭布依族苗族自治县', '台江县'],
    '云南省': ['元阳县', '官渡区', '彝良县', '石林彝族自治县', '丽江地区', '江城哈尼族彝族自治县', '云县', '大姚县',
               '砚山县', '华宁县', '五华区', '景洪市', '玉溪市', '景东彝族自治县', '宣威市',
               '镇沅彝族哈尼族拉祜族自治县', '丽江纳西族自治县', '宁蒗彝族自治县', '丘北县', '西畴县', '中甸县',
               '祥云县', '漾濞彝族自治县', '楚雄彝族自治州', '昭通地区', '大理市', '河口瑶族自治县',
               '兰坪白族普米族自治县', '南华县', '屏边苗族自治县', '南涧彝族自治县', '麻栗坡县', '麒麟区', '通海县',
               '墨江哈尼族自治县', '盈江县', '永德县', '富民县', '绥江县', '呈贡县', '镇雄县', '保山地区', '盘龙区',
               '东川区', '思茅市', '迪庆藏族自治州', '元谋县', '牟定县', '德宏傣族景颇族自治州', '红塔区', '临沧县',
               '红河县', '耿马傣族佤族自治县', '弥渡县', '罗平县', '鲁甸县', '易门县', '晋宁县', '马龙县', '禄丰县',
               '蒙自县', '澄江县', '勐海县', '文山县', '陇川县', '华坪县', '畹町市', '瑞丽市', '维西傈僳族自治县',
               '永胜县', '德钦县', '江川县', '西盟佤族自治县', '鹤庆县', '石屏县', '大关县', '元江哈尼族彝族傣族自治县',
               '普洱哈尼族彝族自治县', '潞西市', '勐腊县', '永善县', '临沧地区', '安宁市', '个旧市',
               '金平苗族瑶族傣族自治县', '会泽县', '剑川县', '泸水县', '镇康县', '景谷傣族彝族自治县',
               '贡山独龙族怒族自治县', '怒江傈僳族自治州', '施甸县', '峨山彝族自治县', '红河哈尼族彝族自治州',
               '沧源佤族自治县', '广南县', '禄劝彝族苗族自治县', '绿春县', '陆良县', '盐津县', '开远市',
               '澜沧拉祜族自治县', '昌宁县', '永平县', '洱源县', '马关县', '姚安县', '双江拉祜族佤族布朗族傣族自治县',
               '昆明市', '云龙县', '西山区', '弥勒县', '水富县', '凤庆县', '福贡县', '武定县', '宾川县', '宜良县',
               '寻甸回族彝族自治县', '巍山彝族回族自治县', '双柏县', '楚雄市', '泸西县', '孟连傣族拉祜族佤族自治县',
               '富宁县', '腾冲县', '巧家县', '富源县', '建水县', '大理白族自治州', '保山市', '威信县', '沾益县',
               '曲靖市', '师宗县', '昭通市', '永仁县', '龙陵县', '嵩明县', '西双版纳傣族自治州', '梁河县',
               '文山壮族苗族自治州', '新平彝族傣族自治县'],
    '西藏省': ['达孜县', '萨嘎县', '吉隆县', '拉孜县', '江达县', '谢通门县', '比如县', '尼玛县', '林周县', '工布江达县',
               '林芝县', '芒康县', '普兰县', '林芝地区', '山南地区', '桑日县', '察雅县', '日喀则市', '曲松县', '措美县',
               '革吉县', '边坝县', '定日县', '噶尔县', '贡嘎县', '拉萨市', '八宿县', '康马县', '日喀则地区', '昂仁县',
               '巴青县', '米林县', '城关区', '曲水县', '萨迦县', '仲巴县', '安多县', '左贡县', '嘉黎县', '措勤县',
               '索县', '定结县', '乃东县', '札达县', '波密县', '南木林县', '浪卡子县', '江孜县', '班戈县', '申扎县',
               '那曲地区', '类乌齐县', '墨竹工卡县', '昌都地区', '仁布县', '阿里地区', '当雄县', '洛扎县', '白朗县',
               '聂拉木县', '岗巴县', '改则县', '琼结县', '朗县', '墨脱县', '贡觉县', '隆子县', '洛隆县', '亚东县',
               '聂荣县', '察隅县', '日土县', '丁青县', '扎囊县', '尼木县', '错那县', '那曲县', '堆龙德庆县', '昌都县',
               '加查县'],
    '陕西省': ['武功县', '白河县', '杨陵区', '米脂县', '延川县', '渭南市', '榆林市', '蒲城县', '富县', '旬阳县',
               '绥德县', '雁塔区', '洛川县', '灞桥区', '宁强县', '宝鸡县', '商南县', '乾县', '宝塔区', '丹凤县',
               '太白县', '宜川县', '白水县', '佳县', '三原县', '临潼区', '安康地区', '合阳县', '永寿县', '周至县',
               '华阴市', '西安市', '韩城市', '秦都区', '蓝田县', '礼泉县', '城区', '清涧县', '榆林地区', '长安县',
               '城固县', '子洲县', '眉县', '高陵县', '佛坪县', '未央区', '宝鸡市', '陇县', '渭城区', '子长县', '兴平市',
               '镇坪县', '户县', '华县', '淳化县', '安康市', '汉中市', '凤县', '镇巴县', '岚皋县', '西乡县', '留坝县',
               '商洛地区', '横山县', '宜君县', '潼关县', '彬县', '汉台区', '平利县', '志丹县', '吴旗县', '紫阳县',
               '富平县', '靖边县', '耀县', '澄城县', '咸阳市', '阎良区', '郊区', '碑林区', '略阳县', '甘泉县', '神木县',
               '安塞县', '麟游县', '旬邑县', '莲湖区', '商州市', '黄陵县', '大荔县', '镇安县', '千阳县', '洋县',
               '宁陕县', '临渭区', '汉阴县', '铜川市', '延安市', '定边县', '洛南县', '岐山县', '府谷县', '新城区',
               '泾阳县', '勉县', '石泉县', '延长县', '柞水县', '南郑县', '金台区', '吴堡县', '黄龙县', '渭滨区',
               '长武县', '凤翔县', '山阳县', '扶风县'],
    '甘肃省': ['定西县', '平川区', '正宁县', '泾川县', '成县', '兰州市', '合水县', '古浪县', '清水县', '西峰市',
               '玉门市', '康县', '两当县', '北道区', '民勤县', '敦煌市', '陇南地区', '武都县', '宁县', '甘南藏族自治州',
               '崇信县', '金昌市', '阿克塞哈萨克族自治县', '景泰县', '夏河县', '秦城区', '迭部县', '临泽县', '秦安县',
               '和政县', '永靖县', '城关区', '酒泉市', '红古区', '积石山保安族东乡族撒拉族自治县', '天水市', '高台县',
               '七里河区', '张家川回族自治县', '漳县', '武威市', '岷县', '宕昌县', '金塔县', '甘谷县', '山丹县',
               '会宁县', '卓尼县', '徽县', '临潭县', '庄浪县', '西固区', '环县', '靖远县', '通渭县', '平凉市', '渭源县',
               '陇西县', '临夏回族自治州', '临洮县', '庆阳县', '安西县', '定西地区', '皋兰县', '肃南裕固族自治县',
               '武威地区', '庆阳地区', '张掖地区', '临夏市', '金川区', '嘉峪关市', '舟曲县', '永登县', '安宁区',
               '酒泉地区', '广河县', '文县', '碌曲县', '东乡族自治县', '张掖市', '镇原县', '肃北蒙古族自治县', '华池县',
               '白银市', '永昌县', '天祝藏族自治县', '礼县', '玛曲县', '平凉地区', '华亭县', '市辖区', '白银区',
               '合作市', '民乐县', '临夏县', '榆中县', '武山县', '灵台县', '静宁县', '西和县', '康乐县'],
    '青海省': ['海南藏族自治州', '甘德县', '治多县', '城中区', '刚察县', '湟源县', '循化撒拉族自治县', '湟中县',
               '达日县', '贵南县', '都兰县', '大通回族土族自治县', '西宁市', '城西区', '民和回族土族自治县', '城东区',
               '果洛藏族自治州', '天峻县', '乐都县', '囊谦县', '杂多县', '城北区', '贵德县', '玉树县', '黄南藏族自治州',
               '兴海县', '共和县', '格尔木市', '尖扎县', '玛多县', '同德县', '称多县', '曲麻莱县', '久治县', '平安县',
               '河南蒙古族自治县', '班玛县', '海北藏族自治州', '海西蒙古族藏族自治州', '德令哈市', '泽库县',
               '玉树藏族自治州', '海东地区', '互助土族自治县', '祁连县', '乌兰县', '化隆回族自治县', '玛沁县', '同仁县',
               '门源回族自治县', '海晏县'],
    '宁夏省': ['中 卫 市', '金凤区', '彭阳县', '\u3000红寺堡区', '青铜峡市', '隆德县', '西夏区', '兴庆区', '西吉县',
               ' 灵武市', '石嘴山市', '平罗县', '泾源县', '永宁县', '吴忠市', ' 中宁县', '大武口区', '贺兰县', '海原县',
               '利通区', '银川市', '沙坡头区', '惠农区', '同心县', '固原地区', '原州区', '盐池县'],
    '新疆省': ['乌尔禾区', '伊犁地区', '乌什县', '省直辖行政单位', '柯坪县', '伽师县', '克孜勒苏柯尔克孜自治州',
               '阿勒泰市', '昌吉市', '托克逊县', '石河子市', '克拉玛依区', '巴音郭楞蒙古自治州', '奎屯市', '精河县',
               '奇台县', '皮山县', '轮台县', '福海县', '木垒哈萨克自治县', '阿瓦提县', '博乐市', '额敏县', '哈密地区',
               '沙雅县', '新市区', '特克斯县', '吉木乃县', '阿合奇县', '沙湾县', '塔城市', '和硕县', '霍城县',
               '吐鲁番市', '疏附县', '阿图什市', '克拉玛依市', '鄯善县', '哈密市', '昌吉回族自治州', '叶城县',
               '头屯河区', '泽普县', '于田县', '白碱滩区', '乌苏市', '阜康市', '和布克赛尔蒙古自治县',
               '察布查尔锡伯自治县', '喀什地区', '昭苏县', '托里县', '墨玉县', '喀什市', '呼图壁县', '尼勒克县',
               '独山子区', '伊宁市', '巴楚县', '布尔津县', '吉木萨尔县', '温泉县', '哈巴河县', '裕民县', '和田县',
               '岳普湖县', '塔什库尔干塔吉克自治县', '阿拉尔市', '且末县', '和田地区', '和田市', '巴里坤哈萨克自治县',
               '吐鲁番地区', '若羌县', '民丰县', '阿克苏地区', '和静县', '天山区', '阿勒泰地区', '疏勒县', '青河县',
               '塔城地区', '巩留县', '焉耆回族自治县', '新和县', '麦盖提县', '莎车县', '温宿县', '博尔塔拉蒙古自治州',
               '伊吾县', '库车县', '阿克陶县', '东山区', '伊犁哈萨克自治州', '乌恰县', '英吉沙县', '尉犁县', '五家渠市',
               '乌鲁木齐市', '洛浦县', '伊宁县', '拜城县', '图木舒克市', '富蕴县', '南山矿区', '阿克苏市', '博湖县',
               '水磨沟区', '库尔勒市', '新源县', '沙依巴克区', '玛纳斯县', '乌鲁木齐县', '策勒县'],
    '台湾省': ['新北市', '台中市', '高雄市', '嘉义市', '基隆市', '台南市', '桃园市', '宜兰县', '台北市', '新竹市'],
    '香港': ['香港'], '澳门': ['澳门']}

a = [['616', '猎鹰蒸汽喷抽清洗机厂家', '2024-12-20 11:43:32', '猎鹰蒸汽喷抽清洗机厂家市场部岳星', '点赞', None,
     '655758904793323', '75568354875', '女', '武汉',
     "家政、汽车精洗综合解决方案服务商，专注于以物理方法解决表面深度清洁问题，纯蒸汽高温高压清洁远离化学污染，有效杀菌除螨除异味，完整的服务流程和配套产品助您打造属于您的特色服务项目！清洁热线18942955144【微信同号】",
     '0', "866", '1981', '18942955144',
     'https://www.douyin.com/user/MS4wLjABAAAAmfMkOm-Fz5JcG0Tu9JCxindRFgv4O8VO7Dga8Ty2F-o',
     'https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_o4eBrAFDtIDOeiAAxaAAfhEpOOQx7TjBaAHmbE.jpeg?from=3067671334',
     '×', None, None], [268, '猎鹰蒸汽喷抽清洗机厂家', '2024-12-20 11:43:39', 'zxf', '进房', None, '2440507320435133',
                        'zxf23135', '-', None, None, '1', '944', '6376', None,
                        'https://www.douyin.com/user/MS4wLjABAAAAL81H9_D_cqfcgCzlJ9CAigyrHlYQNVxm1bc0XBx5ylbvzXVzBIXwalHcVdVn693C',
                        'https://p3.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_3791_5070639578.jpeg?from=3067671334',
                        '×', None, None], ['618', '猎鹰蒸汽喷抽清洗机厂家', '2024-12-20 11:43:44',
                                           '猎鹰蒸汽喷抽清洗机厂家市场部岳星', '发言', '再见[比心][比心]',
                                           '655758904793323', '75568354875', '女', '武汉',
                                           "家政、汽车精洗综合解决方案服务商，专注于以物理方法解决表面深度清洁问题，纯蒸汽高温高压清洁远离化学污染，有效杀菌除螨除异味，完整的服务流程和配套产品助您打造属于您的特色服务项目！清洁热线18942955144【微信同号】",
                                           "0", "866", "1981", "18942955144",
                                           "https://www.douyin.com/user/MS4wLjABAAAAmfMkOm-Fz5JcG0Tu9JCxindRFgv4O8VO7Dga8Ty2F-o",
                                           "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_o4eBrAFDtIDOeiAAxaAAfhEpOOQx7TjjBaAHmbE.jpeg?from=3067671334",
                                           "×", None, None]]

def qx_to_s(qx):
    for s in city_data:
        if qx is not None and type(qx) != 'NoneType':
            h = qx+"市"
            x =  qx + "县"
            z = qx + "镇"
            if qx in city_data[s] or h in city_data[s] or x in city_data[s] or z in city_data[s]:
                print(s)
                return s
    print("未找到该地区所在省份")
    return None


for i in a:
    qx_to_s(i[9])

str = 'Python\\u624d\\u662f\\u4e16\\u754c\\u4e0a\\u6700\\u597d\\u7684\\u8bed\\u8a00'
print(str.encode('utf8').decode('unicode_escape'))
l = '1(10002)'
m = ',18942955144'
print("10002" in l or "10005" in l)
TEST_EXCEL_DIR = "C:\\Users\\ly\\Desktop\\work\\temp"


