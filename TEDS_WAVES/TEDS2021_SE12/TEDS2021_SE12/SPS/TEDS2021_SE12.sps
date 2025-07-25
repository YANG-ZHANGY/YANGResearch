﻿* Encoding: Big5.
DATA LIST FILE="D:\TEDS2021_SE12.DAT " /
NEWID 1-15(A) email 16-55(A) startdate 56-75(A)	submitdate 76-95(A)	
Q1 96-97 Q2 98-99 Q3 100-101 Q4 102-103 Q5 104-105 Q6 106-107
Q7 108-109 Q8 110-111 Q9 112-113 Q10 114-115 Q11 116-117 Q12 118-119
Q13 120-121 Q14 122-123 Q15 124-125 Q16 126-127 Q17 128-129 Q18 130-131
Q19 132-133 Q20 134-135 Q21 136-137 Q22 138-139 Q23 140-141 Q24 142-143
Q25 144-145 Q26 146-147 Q27 148-149 Q28 150-151 Q29 152-153 Q30 154-155
Q31 156-157 Q32 158-159 Q33 160-161 Q34 162-163 Q35 164-165 Q36 166-167
Q37 168-169 Q38 170-171 Q39 172-173 Q40 174-175 Q41 176-177 Q42 178-179
Q43 180-181 Q44 182-183 Q45 184-185 Q46 186-187 Q47 188-189 Q48 190-191
Q49 192-193 Q50 194-195 Q51 196-197 Q52 198-200 Q53 201-203 Q54 204-206
Q55 207-208 Q56 209-210 Q57 211-212 Q58 213-214 Q59 215-216 Q60 217-218
Q61 219-220 Q62 221-222 Q63 223-224 Q64 225-226 Q65 227-228 Q66 229-230
Q67 231-232 Q68 233-234 Q69 235-236 Q70 237-238 Q71 239-240 Q72 241-242
Q73 243-244 Q74 245-246 Q75 247-248 Q76 249-250 Q77 251-252 Q78 253-254 Q79 255-256.

VARIABLE LABELS
NEWID "樣本編號"
EMAIL "電子郵件信箱"
startdate "填答開始時間"
datestamp "填答結束時間"
Q1 "整體來說，請問您對政治的事情，感不感興趣?"
Q2 "請問您對蔡英文總統的整體表現滿不滿意?"
Q3 "請問從今年五月中疫情爆發以來，您家庭的經濟狀況與以前相比是變的比較好、比較差還是差不多?"
Q4 "請問從今年五月中疫情爆發以來，您認為臺灣現在的經濟狀況與以前相比是變的比較好、比較差還是差不多?"
Q5 "請問您對政府在處理新冠肺炎疫情的表現滿不滿意?"
Q6 "請問您在臺灣接種過新冠肺炎的疫苗了嗎?"
Q7 "請問您已經打了一劑還是兩劑?"
Q8 "請問您第一劑是施打哪個廠牌的疫苗?"
Q9 "請問您第二劑是施打哪個廠牌的疫苗?"
Q10 "有人說: 「政治有時候太複雜了，所以我們一般民眾實在搞不懂」，請問您同不同意這個看法?"
Q11 "有人說: 「我們一般民眾對政府的作為，沒有任何影響力」。"
Q12 "有人說: 「政府官員不會在乎我們一般民眾的想法」。"
Q13 "有人說: 「公民投票的議題有時候太複雜了，所以我們一般民眾實在搞不懂」。"
Q14 "有人說: 「政府所做的事情大部分是正確的」。"
Q15 "有人說: 「政府官員時常浪費一般民眾所繳納的稅金」。"
Q16 "請問您認為政府決定重大政策時，會不會把「民眾的福利」放在第一優先考慮的地位?是經常會考慮、有時會考慮、不太會考慮、還是絕對不會考慮?"
Q17 "您會給國民黨多少?"
Q18 "您會給民進黨多少?"
Q19 "您會給台灣民眾黨多少?"
Q20 "您會給朱立倫多少?"
Q21 "您會給柯文哲多少?"
Q22 "您會給賴清德多少?"
Q23 "您會給鄭文燦多少?"
Q24 "您會給郭台銘多少?"
Q25 "每逢投票，有人會去投票；有人因為太忙或其他原因不去投票，也有人對投票完全不感興趣，也有人用不投票來表達意見。請問今年(2021年)12月18日的公民投票，您有沒有去投票?"
Q26 "請問您，公民投票第17案: 「您是否同意核四啟封商轉發電」(即「核四商轉」公投案)，您是投同意還是不同意?"
Q27 "那麼，公民投票第18案: 「你是否同意政府應全面禁止進口含有萊克多巴胺之乙型受體素豬隻之肉品、內臟及其相關產製品?」(即「反萊豬」公投案)，您是投同意還是不同意?"
Q28 "那麼，公民投票第19案: 「你是否同意公民投票案公告成立後半年內，若該期間內遇有全國性選舉時，在符合公民投票法規定之情形下，公民投票應與該選舉同日舉行?」(即「公投綁大選」公投案)，您是投同意還是不同意?"
Q29 "那麼，公民投票第20案: 「您是否同意中油第三天然氣接收站遷離桃園大潭藻礁海岸及海域?(即北起觀音溪出海口，南至新屋溪出海口之海岸，及由上述海岸最低潮線往外平行延伸五公里之海域)」(即「珍愛藻礁」公投案)，您是投同意還是不同?意"
Q30 "如果您有去投票，請問您，公民投票第17案: 「您是否同意核四啟封商轉發電」(即「核四商轉」公投案)，您會投同意還是不同意?"
Q31 "那麼，公民投票第18案: 「你是否同意政府應全面禁止進口含有萊克多巴胺之乙型受體素豬隻之肉品、內臟及其相關產製品?」(即「反萊豬」公投案)，您會投同意還是不同意?"
Q32 "那麼，公民投票第19案: 「你是否同意公民投票案公告成立後半年內，若該期間內遇有全國性選舉時，在符合公民投票法規定之情形下，公民投票應與該選舉同日舉行?」(即「公投綁大選」公投案)，您是投同意還是不同意?"
Q33 "那麼，公民投票第20案: 「您是否同意中油第三天然氣接收站遷離桃園大潭藻礁海岸及海域?(即北起觀音溪出海口，南至新屋溪出海口之海岸，及由上述海岸最低潮線往外平行延伸五公里之海域)」(即「珍愛藻礁」公投案)，您是投同意還是不同意?"
Q34 "在今年(2021年)12月18日的公民投票期間，請問您最主要是從哪裡獲得公民投票案的相關消息的?"
Q35 "那其次呢?"
Q36 "有人主張把公職人員(包含村里長、民意代表、總統等)選舉的投票年齡從目前的20歲修改為18歲，請問您同不同意這樣的主張?"
Q37 "我們社會上有人主張修改憲法，廢除考試院，請問您同不同意這樣的主張?"
Q38 "那麼有人主張廢除監察院，請問您同不同意這樣的主張?"
Q39 "那麼有人主張總統提名的行政院長人選須經由立法院同意後才能上任，請問您同不同意這樣的主張?"
Q40 "請問去年(2020年)1月11日的總統選舉，您是投給哪一組候選人?"
Q41 "那請問您不分區立委的選票投給哪一個政黨?"
Q42 "請問，2018年11月的公民投票，您有沒有去投票?"
Q43 "請問在第9案的「反核食」議題的公投票，您是投同意或不同意?主文: 你是否同意政府維持禁止開放日本福島311核災相關地區，包括福島與周遭4縣市(茨城、櫪木、群馬、千葉)等地區農產品及食品進口?"
Q44 "請問在第13案的「東京奧運台灣正名」議題的公投票，您是投同意或不同意?主文: 你是否同意，以「台灣」為全名申請參加所有國際運動賽事及2020年東京奧運?"
Q45 "請問在第16案的「以核養綠」議題的公投票，您是投同意或不同意?主文: 你是否同意廢除《電業法》第95條第1項，即「廢除核能發電設備應於中華民國一百十四年以前，全部停止運轉」之條文?"
Q46 "關於台灣和大陸的關係，有下面幾種不同的看法。請問您比較偏向哪一種?"
Q47 "在目前國內的政黨之中，請問您認為您比較支持哪一個政黨?"
Q48 "請問您支持(Q47)的程度是非常支持，還是普普通通?"
Q49 "那請問您有沒有比較偏向哪一個政黨?"
Q50 "我們社會有人說自己是台灣人，也有人說自己是中國人，也有人說都是。請問您認為自己是台灣人、中國人，或者都是?"
Q51 "請問您的最高學歷是什麼(讀到什麼學校)?"
Q52 "請問您的職業是?"
Q53 "請問您先生(或太太)的職業是什麼?"
Q54 "請問您以前(或退休前)的職業是什麼?"
Q55 "您的戶籍是設在______縣市?"
Q56 "請問在宜蘭縣那一個鄉鎮市?"
Q57 "請問在新竹縣那一個鄉鎮市?"
Q58 "請問在苗栗縣那一個鄉鎮市?"
Q59 "請問在彰化縣那一個鄉鎮市?"
Q60 "請問在南投縣那一個鄉鎮市?"
Q61 "請問在雲林縣那一個鄉鎮市?"
Q62 "請問在嘉義縣那一個鄉鎮市?"
Q63 "請問在屏東縣那一個鄉鎮市?"
Q64 "請問在臺東縣那一個鄉鎮市?"
Q65 "請問在花蓮縣那一個鄉鎮市?"
Q66 "請問在澎湖縣那一個鄉鎮市?"
Q67 "請問在基隆市那一個區?"
Q68 "請問在新竹市那一個區?"
Q69 "請問在嘉義市那一個區?"
Q70 "請問在臺北市那一個區?"
Q71 "請問在高雄市那一個區?"
Q72 "請問在新北市那一個區?"
Q73 "請問在臺中市那一個區?"
Q74 "請問在臺南市那一個區?"
Q75 "請問在桃園市那一個區?"
Q76 "請問在金門縣那一個鄉鎮市?"
Q77 "請問在連江縣那一個鄉鎮市?"
Q78 "請問您現在是否居住在戶籍地?"
Q79 "性別".

VALUE LABELS
/Email
      1 "Email"
/Q1
 01 "非常有興趣"     02 "有點興趣"     03 "不太有興趣"     04 "完全沒興趣"
 96 "很難說"            97 "無意見"        98 "不知道"           95 "拒答"
/Q2
 01 "非常滿意"         02 "有點滿意"     03 "不太滿意"        04 "非常不滿意"
 96 "很難說"            97 "無意見"         98 "不知道"           95 "拒答"
/Q3
 01 "好很多"            02 "比較好"        03 "差不多"            04 "比較差"            05 "非常差"
 96 "看情形"            97 "無意見"        98 "不知道"            95 "拒答"
/Q4
 01 "好很多"            02 "比較好"        03 "差不多"            04 "比較差"            05 "非常差"
 96 "看情形"            97 "無意見"        98 "不知道"            95 "拒答"
/Q5
 01 "非常滿意"         02 "有點滿意"     03 "不太滿意"        04 "非常不滿意"
 96 "很難說"            97 "無意見"         98 "不知道"           95 "拒答"
/Q6
 01 "有"                  02 "沒有"            95 "拒答"
/Q7
 01 "一劑"               02 "兩劑"           
 95 "拒答"               99 "跳題"
/Q8
 01 "AstraZeneca(AZ)"         02 "Moderna(莫德納)"          03 "高端"         04 "BNT(輝瑞)"             05 "Johnson&Johnson(嬌生)"
 06 "聯亞"                           07 "科興"                            08 "國藥"
 95 "拒答"                           99 "跳題"
/Q9
 01 "AstraZeneca(AZ)"         02 "Moderna(莫德納)"          03 "高端"         04 "BNT(輝瑞)"             05 "Johnson&Johnson(嬌生)"
 06 "聯亞"                          07 "科興"                            08 "國藥"
 95 "拒答"                           99 "跳題"
/Q10
 01 "非常同意"           02 "同意"              03 "不同意"           04 "非常不同意"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q11
 01 "非常同意"           02 "同意"              03 "不同意"           04 "非常不同意"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q12
 01 "非常同意"           02 "同意"              03 "不同意"           04 "非常不同意"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q13
 01 "非常同意"           02 "同意"              03 "不同意"           04 "非常不同意"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q14
 01 "非常同意"           02 "同意"              03 "不同意"           04 "非常不同意"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q15
 01 "非常同意"           02 "同意"              03 "不同意"           04 "非常不同意"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q16
 01 "經常會考慮"       02 "有時會考慮"     03 "不太會考慮"     04 "絕對不會考慮"
 96 "看情形"              97 "無意見"           98 "不知道"           95 "拒答"
/Q17
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q18
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q19
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q20
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q21
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q22
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q23
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q24
 0 "非常不喜歡"         10 "非常喜歡" 
 98 "不知道"              95 "拒答"
/Q25
 01 "有"                     02 "沒有" 
 95 "拒答"
/Q26
 01 "同意"               02 "不同意" 
  89 "未領這張票"    94 "投廢票"        95 "拒答"         99 "跳題"
/Q27
 01 "同意"               02 "不同意" 
  89 "未領這張票"    94 "投廢票"        95 "拒答"         99 "跳題"
/Q28
 01 "同意"               02 "不同意" 
  89 "未領這張票"    94 "投廢票"        95 "拒答"         99 "跳題"
/Q29
 01 "同意"               02 "不同意" 
  89 "未領這張票"    94 "投廢票"        95 "拒答"         99 "跳題"
/Q30
 01 "同意"                        02 "不同意" 
 89 "不會領這張公投票"     94 "投廢票"      95 "拒答"     99 "跳題"
/Q31
 01 "同意"                        02 "不同意" 
 89 "不會領這張公投票"     94 "投廢票"      95 "拒答"     99 "跳題"
/Q32
 01 "同意"                        02 "不同意" 
 89 "不會領這張公投票"     94 "投廢票"      95 "拒答"     99 "跳題"
/Q33
 01 "同意"                        02 "不同意" 
 89 "不會領這張公投票"     94 "投廢票"      95 "拒答"     99 "跳題"
/Q34
 01 "電視新聞"          02 "政論節目"               03 "廣播"                   04 "網路新聞"               05 "政黨網站"
 06 "報紙"                 07 "親朋好友"               08 "社群媒體(例如:YouTube、LINE、Facebook、Instagram)"
 09 "里長"                10 "簡訊(含電話語音)"    11 "宣傳車或文宣"     12 "社團組織"
 13 "同事"                14 "電視公民投票案意見發表會"                     15 "政黨公投說明會" 
 16 "公投公報"          17 "自行上網搜尋"
 91 "都有"                 92 "都沒有"                   95 "拒答"
/Q35
 01 "電視新聞"          02 "政論節目"               03 "廣播"                   04 "網路新聞"               05 "政黨網站"
 06 "報紙"                 07 "親朋好友"               08 "社群媒體(例如:YouTube、LINE、Facebook、Instagram)"
 09 "里長"                10 "簡訊(含電話語音)"    11 "宣傳車或文宣"     12 "社團組織"
 13 "同事"                14 "電視公民投票案意見發表會"                     15 "政黨公投說明會" 
 16 "公投公報"          17 "自行上網搜尋"
 92 "沒有了"              95 "拒答"                      99 "跳題"
/Q36
 01 "同意"                 02 "不同意"
 96 "很難說"              97 "無意見"                   98 "不知道"               95 "拒答"
/Q37
 01 "同意"                 02 "不同意"
 96 "很難說"              97 "無意見"                   98 "不知道"               95 "拒答"
/Q38
 01 "同意" 02 "不同意"
 96 "很難說" 97 "無意見" 98 "不知道" 95 "拒答"
/Q39
 01 "同意"                 02 "不同意"
 96 "很難說"              97 "無意見"                   98 "不知道"               95 "拒答"
/Q40
 01 "宋楚瑜、余湘"    02 "韓國瑜、張善政"       03 "蔡英文、賴清德"
 89 "無投票權"           91 "忘記了"                   92 "未領票"               94 "投廢票"     95 "拒答"        93 "沒去投"
/Q41
 01 "國民黨"            02 "民進黨"            03 "新黨"               04 "親民黨"                06 "台灣團結聯盟"
 09 "綠黨"               13 "勞動黨"            17 "台灣基進"         19 "時代力量"             25 "中華統一促進黨"
 37 "國會政黨聯盟"  38 "合一行動聯盟"   39 "安定力量"         40 "宗教聯盟"            41 "台灣民眾黨"
 42 "台灣維新"         43 "台澎黨"            44 "喜樂島聯盟"      45 "一邊一國行動黨"
 89 "未領票"            91 "忘記了"            94 "投廢票"            95 "拒答"                    99 "跳題"
/Q42
 01 "有"                   02 "沒有" 
 92 "當時沒投票權"   95 "拒答"
/Q43
 01 "同意"                02 "不同意" 
 89 "沒領票"             91 "忘記了"             95 "拒答"               99 "跳題"
/Q44
 01 "同意"                02 "不同意" 
 89 "沒領票"             91 "忘記了"             95 "拒答"               99 "跳題"
/Q45
 01 "同意"                02 "不同意" 
 89 "沒領票"             91 "忘記了"             95 "拒答"               99 "跳題"
/Q46
 01 "儘快統一"                                           02 "儘快宣布獨立"
 03 "維持現狀，以後走向統一"                    04 "維持現狀，以後走向獨立"
 05 "維持現狀，看情形再決定獨立或統一"    06 "永遠維持現狀"
 07 "已經是個獨立的國家"
 96 "很難說"               97 "無意見"              98 "不知道"                    95 "拒答"
/Q47
 01 "國民黨"           02 "民進黨"             03 "新黨"            04 "親民黨"             05 "台聯"
 20 "綠黨"              21 "時代力量"          23 "社民黨"         35 "台灣基進"         38 "台灣民眾黨"
 06 "都支持"           07 "都不支持"          19 "選人不選黨"
 96 "看情形"           97 "無意見"              98 "不知道"         95 "拒答"
/Q48
 01 "非常支持"        02 "普普通通" 
 99 "跳題"
/Q49
 03 "偏國民黨"        04 "偏民進黨"           05 "偏新黨"          06 "偏親民黨"         07 "偏台聯"
 23 "偏綠黨"           24 "偏時代力量"        26 "偏社民黨"       38 "偏台灣基進"      41 "偏台灣民眾黨"
 08 "都不偏"           21 "選人不選黨"
 96 "看情形"           97 "無意見"               98 "不知道"          95 "拒答"                99 "跳題"
/Q50
 01 "台灣人"           02 "中國人"               03 "都是"
 96 "很難說"           97 "無意見"               98 "不知道"           95 "拒答"
/Q51
 01 "不識字及未入學"       02 "小學"          03 "國、初中"        04 "高中、職"             05 "專科"                        
 06 "大學"                       07 "研究所及以上"
 95 "拒答"
/Q52
 101 "民意代表"          102 "政府行政主管"       103 "公營事業主管"       104 "民營事業主管"
 105 "民營事業公司負責人(自營商人)，有雇用人"                                 106 "民營事業公司負責人(自營商人)，沒有雇用人"
 201 "政府部門研究人員(科學家)"                                                        202 "私人部門研究人員(科學家)"
 203 "公立醫療單位醫事技術人員(醫師、藥師、護士、醫療人員)"          204 "非公立醫療單位醫事技術人員(醫師、藥師、護士、醫療人員)"
 205 "會計師"                                                                                    206 "公立教育機構教師"                                       
 207 "私立教育機構教師"                                                                    208 "法官、書記官、檢察官、司法官"                  
 209 "律師"                                                                                        210 "宗教工作者" 
 211 "藝術工作者(演員、表演工作者、攝影師)"                                     212 "文字工作者(作家、記者、劇作家)"                 
 213 "公營事業工程師(機師)"                                                               214 "民營事業工程師(機師)"                                  
 215 "職業運動專業人士"                                                                     
 301 "政府單位與公營事業部門職員"                                                    302 "民營事業職員"
 303 "買賣業務人員"                                             
 401 "服務、餐旅人員(含攤販、個人服務、計程車司機)"                         501 "農林漁牧"                                                 
 601 "政府單位與公營事業部門勞工"                                                     602 "民營事業勞工"                                             
 701 "學生"                                                                                         801 "軍警調查局人員"                                           
 901 "家管，沒有做家庭代工"                                                               902 "家管，有做家庭代工"
 903 "家管，家裡有事業，有幫忙但未領薪水"                                        904 "家管，家裡有事業，有幫忙且領薪水"
 905 "失業者"                               906 "退休者"                                    907 "無正式工作但有其他收入"   
 908 "家管，有做網拍或代購"        911 "一直無業"                                 995 "拒答"
/Q53
 101 "民意代表"          102 "政府行政主管"       103 "公營事業主管"       104 "民營事業主管"
 105 "民營事業公司負責人(自營商人)，有雇用人"                                 106 "民營事業公司負責人(自營商人)，沒有雇用人"
 201 "政府部門研究人員(科學家)"                                                        202 "私人部門研究人員(科學家)"
 203 "公立醫療單位醫事技術人員(醫師、藥師、護士、醫療人員)"          204 "非公立醫療單位醫事技術人員(醫師、藥師、護士、醫療人員)"
 205 "會計師"                                                                                    206 "公立教育機構教師"    
 207 "私立教育機構教師"                                                                    208 "法官、書記官、檢察官、司法官"   
 209 "律師"                                                                                        210 "宗教工作者"     
 211 "藝術工作者(演員、表演工作者、攝影師)"                                     212 "文字工作者(作家、記者、劇作家)"
 213 "公營事業工程師(機師)"                                                               214 "民營事業工程師(機師)"
 215 "職業運動專業人士"
 301 "政府單位與公營事業部門職員"                                                    302 "民營事業職員"
 303 "買賣業務人員"        
 401 "服務、餐旅人員(含攤販、個人服務、計程車司機)"                         501 "農林漁牧"
 601 "政府單位與公營事業部門勞工"                                                     602 "民營事業勞工"
 701 "學生"                                                                                        801 "軍警調查局人員"
 901 "配偶已去逝" 902 "沒有配偶(含已離異)"                                        907 "無正式職業，但有其他收入"
 995 "拒答"                                                                                        999 "跳題"
/Q54
 101 "民意代表"          102 "政府行政主管"       103 "公營事業主管"       104 "民營事業主管"
 105 "民營事業公司負責人(自營商人)，有雇用人"                                 106 "民營事業公司負責人(自營商人)，沒有雇用人"
 201 "政府部門研究人員(科學家)"                                                        202 "私人部門研究人員(科學家)"
 203 "公立醫療單位醫事技術人員(醫師、藥師、護士、醫療人員)"          204 "非公立醫療單位醫事技術人員(醫師、藥師、護士、醫療人員)"
 205 "會計師"                                                                                    206 "公立教育機構教師"    
 207 "私立教育機構教師"                                                                    208 "法官、書記官、檢察官、司法官"   
 209 "律師"                                                                                        210 "宗教工作者"     
 211 "藝術工作者(演員、表演工作者、攝影師)"                                     212 "文字工作者(作家、記者、劇作家)"
 213 "公營事業工程師(機師)"                                                               214 "民營事業工程師(機師)"
 215 "職業運動專業人士"
 301 "政府單位與公營事業部門職員"                                                    302 "民營事業職員"
 303 "買賣業務人員"        
 401 "服務、餐旅人員(含攤販、個人服務、計程車司機)"                         501 "農林漁牧"
 601 "政府單位與公營事業部門勞工"                                                     602 "民營事業勞工"
 701 "學生"                                                                                        801 "軍警調查局人員"
 907 "無正式工作但有其他收入"
 995 "拒答"                                                                                         999 "跳題"   
/Q55
 2 "宜蘭縣"    4 "新竹縣"    5 "苗栗縣"    7 "彰化縣"    8 "南投縣"    
 9 "雲林縣"    10 "嘉義縣"   13 "屏東縣"   14 "臺東縣"   15 "花蓮縣"   
 16 "澎湖縣"   17 "基隆市"   18 "新竹市"   20 "嘉義市"   28 "金門縣" 
 30 "連江縣"  
 63 "臺北市"   64 "高雄市"   65 "新北市"   66 "臺中市"   67 "臺南市"   
 68 "桃園市"   98 "不知道"   95 "拒答"
/Q56
 1 "宜蘭市"    2 "羅東鎮"    3 "蘇澳鎮"    4 "頭城鎮"    5 "礁溪鄉"
 6 "壯圍鄉"    7 "員山鄉"    8 "冬山鄉"    9 "五結鄉"    10 "三星鄉"
 11 "大同鄉"   12 "南澳鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q57
 1 "竹北市"    2 "竹東鎮"    3 "新埔鎮"    4 "關西鎮"    5 "湖口鄉"
 6 "新豐鄉"    7 "芎林鄉"    8 "橫山鄉"    9 "北埔鄉"    10 "寶山鄉"
 11 "峨眉鄉"   12 "尖石鄉"   13 "五峰鄉"   98 "不知道"
 95 "拒答"     99 "跳題"
/Q58
 1 "苗栗市"    2 "苑裡鎮"    3 "通霄鎮"    4 "竹南鎮"    5 "頭份市"
 6 "後龍鎮"    7 "卓蘭鎮"    8 "大湖鄉"    9 "公館鄉"    10 "銅鑼鄉"
 11 "南庄鄉"   12 "頭屋鄉"   13 "三義鄉"   14 "西湖鄉"   15 "造橋鄉"
 16 "三灣鄉"   17 "獅潭鄉"   18 "泰安鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q59
 1 "彰化市"    2 "鹿港鎮"    3 "和美鎮"    4 "線西鄉"    5 "伸港鄉"
 6 "福興鄉"    7 "秀水鄉"    8 "花壇鄉"    9 "芬園鄉"    10 "員林市"
 11 "溪湖鎮"   12 "田中鎮"   13 "大村鄉"   14 "埔鹽鄉"   15 "埔心鄉"
 16 "永靖鄉"   17 "社頭鄉"   18 "二水鄉"   19 "北斗鎮"   20 "二林鎮"
 21 "田尾鄉"   22 "埤頭鄉"   23 "芳苑鄉"   24 "大城鄉"   25 "竹塘鄉"
 26 "溪州鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q60
 1 "南投市"    2 "埔里鎮"    3 "草屯鎮"    4 "竹山鎮"    5 "集集鎮"
 6 "名間鄉"    7 "鹿谷鄉"    8 "中寮鄉"    9 "魚池鄉"    10 "國姓鄉"
 11 "水里鄉"   12 "信義鄉"   13 "仁愛鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q61
 1 "斗六市"    2 "斗南鎮"    3 "虎尾鎮"    4 "西螺鎮"    5 "土庫鎮"
 6 "北港鎮"    7 "古坑鄉"    8 "大埤鄉"    9 "莿桐鄉"    10 "林內鄉"
 11 "二崙鄉"   12 "崙背鄉"   13 "麥寮鄉"   14 "東勢鄉"   15 "褒忠鄉"
 16 "臺西鄉"   17 "元長鄉"   18 "四湖鄉"   19 "口湖鄉"   20 "水林鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q62
 1 "太保市"    2 "朴子市"    3 "布袋鎮"    4 "大林鎮"    5 "民雄鄉"
 6 "溪口鄉"    7 "新港鄉"    8 "六腳鄉"    9 "東石鄉"    10 "義竹鄉"
 11 "鹿草鄉"   12 "水上鄉"   13 "中埔鄉"   14 "竹崎鄉"   15 "梅山鄉"
 16 "番路鄉"   17 "大埔鄉"   18 "阿里山鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q63
 1 "屏東市"    2 "潮洲鎮"    3 "東港鎮"    4 "恆春鎮"    5 "萬丹鄉"
 6 "長治鄉"    7 "麟洛鄉"    8 "九如鄉"    9 "里港鄉"    10 "鹽埔鄉"
 11 "高樹鄉"   12 "萬巒鄉"   13 "內埔鄉"   14 "竹田鄉"   15 "新埤鄉"
 16 "枋寮鄉"   17 "新園鄉"   18 "崁頂鄉"   19 "林邊鄉"   20 "南州鄉"
 21 "佳冬鄉"   22 "琉球鄉"   23 "車城鄉"   24 "滿州鄉"   25 "枋山鄉"
 26 "三地門鄉" 27 "霧臺鄉"   28 "瑪家鄉"   29 "泰武鄉"   30 "來義鄉"
 31 "春日鄉"   32 "獅子鄉"   33 "牡丹鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q64
 1 "臺東市"    2 "成功鎮"    3 "關山鎮"    4 "卑南鄉"    5 "鹿野鄉"
 6 "池上鄉"    7 "東河鄉"    8 "長濱鄉"    9 "太麻里鄉"  10 "大武鄉"
 11 "綠島鄉"   12 "海端鄉"   13 "延平鄉"   14 "金峰鄉"   15 "達仁鄉"
 16 "蘭嶼鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q65
 1 "花蓮市"    2 "鳳林鎮"    3 "玉里鎮"    4 "新城鄉"    5 "吉安鄉"
 6 "壽豐鄉"    7 "光復鄉"    8 "豐濱鄉"    9 "瑞穗鄉"    10 "富里鄉"
 11 "秀林鄉"   12 "萬榮鄉"   13 "卓溪鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q66
 1 "馬公市"    2 "湖西鄉"    3 "白沙鄉"    4 "西嶼鄉"    5 "望安鄉"
 6 "七美鄉"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q67
 1 "中正區"    2 "七堵區"    3 "暖暖區"    4 "仁愛區"    5 "中山區"
 6 "安樂區"    7 "信義區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q68
 1 "東區" 2 "北區" 3 "香山區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q69
 1 "東區" 2 "西區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q70
 1 "松山區"    2 "信義區"    3 "大安區"    4 "中山區"    5 "中正區"
 6 "大同區"    7 "萬華區"    8 "文山區"    9 "南港區"    10 "內湖區"
 11 "士林區"   12 "北投區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q71
 1 "鹽埕區"    2 "鼓山區"    3 "左營區"    4 "楠梓區"    5 "三民區"
 6 "新興區"    7 "前金區"    8 "苓雅區"    9 "前鎮區"    10 "旗津區"
 11 "小港區"   12 "鳳山區"   13 "林園區"   14 "大寮區"   15 "大樹區"
 16 "大社區"   17 "仁武區"   18 "鳥松區"   19 "岡山區"   20 "橋頭區"
 21 "燕巢區"   22 "田寮區"   23 "阿蓮區"   24 "路竹區"   25 "湖內區"
 26 "茄萣區"   27 "永安區"   28 "彌陀區"   29 "梓官區"   30 "旗山區"
 31 "美濃區"   32 "六龜區"   33 "甲仙區"   34 "杉林區"   35 "內門區"
 36 "茂林區"   37 "桃源區"   38 "那瑪夏區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q72
 1 "板橋區"    2 "三重區"    3 "中和區"    4 "永和區"    5 "新莊區"
 6 "新店區"    7 "樹林區"    8 "鶯歌區"    9 "三峽區"    10 "淡水區"
 11 "汐止區"   12 "瑞芳區"   13 "土城區"   14 "蘆洲區"   15 "五股區"
 16 "泰山區"   17 "林口區"   18 "深坑區"   19 "石碇區"   20 "坪林區"
 21 "三芝區"   22 "石門區"   23 "八里區"   24 "平溪區"   25 "雙溪區"
 26 "貢寮區"   27 "金山區"   28 "萬里區"   29 "烏來區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q73
 1 "中區" 2 "東區" 3 "南區" 4 "西區" 5 "北區"
 6 "西屯區"    7 "南屯區"    8 "北屯區"    9 "豐原區"    10 "東勢區"
 11 "大甲區"   12 "清水區"   13 "沙鹿區"   14 "梧棲區"   15 "后里區"
 16 "神岡區"   17 "潭子區"   18 "大雅區"   19 "新社區"   20 "石岡區"
 21 "外埔區"   22 "大安區"   23 "烏日區"   24 "大肚區"   25 "龍井區"
 26 "霧峰區"   27 "太平區"   28 "大里區"   29 "和平區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q74
 1 "新營區"    2 "鹽水區"    3 "白河區"    4 "柳營區"    5 "後壁區"
 6 "東山區"    7 "麻豆區"    8 "下營區"    9 "六甲區"    10 "官田區"
 11 "大內區"   12 "佳里區"   13 "學甲區"   14 "西港區"   15 "七股區"
 16 "將軍區"   17 "北門區"   18 "新化區"   19 "善化區"   20 "新市區"
 21 "安定區"   22 "山上區"   23 "玉井區"   24 "楠西區"   25 "南化區"
 26 "左鎮區"   27 "仁德區"   28 "歸仁區"   29 "關廟區"   30 "龍崎區"
 31 "永康區"   32 "東區"     33 "南區"     34 "北區"     35 "安南區"
 36 "安平區"   37 "中西區"
 98 "不知道"   95 "拒答"     99 "跳題"
/Q75
 1 "桃園區"    2 "中壢區"    3 "大溪區"    4 "楊梅區"    5 "蘆竹區"
 6 "大園區"    7 "龜山區"    8 "八德區"    9 "龍潭區"    10 "平鎮區"
 11 "新屋區"   12 "觀音區"   13 "復興區"   98 "不知道"
 95 "拒答"     99 "跳題"
/Q76
 1 "金城鎮"    2 "金沙鎮"    3 "金湖鎮"    4 "金寧鄉"    5 "烈嶼鄉"
 6 "烏坵鄉"
 98 "不知道"   95 "拒答"     99 "跳題" 
/Q77
 1 "南竿鄉"    2 "北竿鄉"    3 "莒光鄉"    4 "東引鄉"
 98 "不知道"   95 "拒答"     99 "跳題" 
/Q78
 1 "是"   2 "否"   95 "拒答"
/Q79
 1 "男性"     2 "女性".

fre all.


*[建立性別新變數].
COMPUTE SEX=q79.
variable label SEX "性別".
value label SEX 1 "男性" 2 "女性".
cro q79 by SEX.


*年齡.
compute AGE=110-BIRTH.
recode AGE (lo thru 19=1)(20 thru 29=2)(30 thru 39=3)(40 thru 49=4)(50 thru 59=5) (60 thru hi=6).
var lab AGE "年齡".
val lab AGE 1 "18至19歲" 2 "20至29歲" 3 "30至39歲" 4 "40至49歲" 5 "50至59歲" 6 "60歲及以上".
cross BIRTH by AGE.
fre AGE.

*教育程度.
compute EDU=q51.
recode EDU (1 2=1) (3=2) (4=3) (5=4) (6 7=5) (ELSE=9).
var lab EDU "教育程度".
val lab EDU 1 "小學及以下" 2 "國、初中" 3 "高中、職" 4 "專科" 5 "大學及以上" 9 "無反應".
fre EDU.

*[建立職業五分類新變數].
COMPUTE AA=Q52.                                                                      
COMPUTE BB=Q53.                                                                      
COMPUTE CC=Q54.                                                                      
COMPUTE DD=Q54.                                                                      
COMPUTE EE=Q52.                                                                      
RECODE AA (101 THRU 106=1)(201 THRU 215=2)(301 THRU 303=3)(401=4)(501=5)             
          (601 602=6)(701=7)(801=8)(901 THRU 904=9)(906 905=10).                     
RECODE BB (101 THRU 215=1)(701 801=1) (301 THRU 401=2)(501=3)(601 602=4)(ELSE=5).    
RECODE CC (101 THRU 215=1)(701 801=1) (301 THRU 401=2)(501=3)(601 602=4)(ELSE=5).    
RECODE DD (101 102 103 201 203 206 208 213 301 601 801 207=1)                        
          (104 106 105 202 204 205 209 210 211 212 214 215=2)                        
          (302 303 401=3)(602=4)(501=5)(701=6)(901 THRU 904=7)(ELSE=8).              
RECODE EE (101 THRU 106=1)(201 THRU 215=2)(301 THRU 303=3)(401=4)(501=5)             
          (601 602=6)(701=7)(801=8)(901 THRU 904=9)(906=10).                         

COMPUTE CAREER=Q52.                                                                  
RECODE CAREER (101 THRU 215=1)(701 801=1)                                            
              (301 THRU 401=2)(501=3)(601 602=4)(ELSE=5).                            
IF (AA=9  AND BB=1) CAREER=1.                                                        
IF (AA=9  AND BB=2) CAREER=2.                                                        
IF (AA=9  AND BB=3) CAREER=3.                                                        
IF (AA=9  AND BB=4) CAREER=4.                                                        
IF (AA=9  AND BB>4) CAREER=5.                                                        
IF (AA=10 AND CC=1) CAREER=1.                                                        
IF (AA=10 AND CC=2) CAREER=2.                                                        
IF (AA=10 AND CC=3) CAREER=3.                                                        
IF (AA=10 AND CC=4) CAREER=4.                                                        
IF (AA=10 AND CC>4) CAREER=5.                                                        
VARIABLE LABELS CAREER "職業五分類".                                                 
VALUE LABELS CAREER 1 "高、中級白領" 2 "中低、低級白領" 3 "農林漁牧" 4 "藍領"        
                    5 "無反應、其他".                                                        
fre CAREER.                                                                          
                                                                                              
                                                                                              
*建立職業八分類變數.                                                                          
COMPUTE CAREER8=Q52.                                                                          
RECODE CAREER8 (101 102 103 201 203 206 208 213 301 601 801 207=1)                            
               (104 106 105 202 204 205 209 210 211 212 214 215=2)                            
               (302 303 401=3)(602=4)(501=5)(701=6)(901 THRU 904=7)                           
               (ELSE=8).                                                                      
IF (AA=10 AND DD=1) CAREER8=1.                                                                
IF (AA=10 AND DD=2) CAREER8=2.                                                                
IF (AA=10 AND DD=3) CAREER8=3.                                                                
IF (AA=10 AND DD=4) CAREER8=4.                                                                
IF (AA=10 AND DD=5) CAREER8=5.                                                                
IF (AA=10 AND DD=6) CAREER8=6.                                                                
IF (AA=10 AND DD=7) CAREER8=7.                                                                
IF (AA=10 AND DD>7) CAREER8=8.                                                                
VARIABLE LABELS CAREER8 "職業八分類".                                                         
VALUE LABELS CAREER8 1 "軍公教人員" 2 "私部門管理階層及專業人員" 3 "私部門職員"               
                     4 "私部門勞工" 5 "農林漁牧" 6 "學生" 7 "家管"                            
                     8 "無反應、其他".                                                                          
fre CAREERr8.                                                                                  
delete var aa bb cc dd ee.

*[建立戶籍新變數].                                                                  
COMPUTE TOWNID=0.                                                                                
COMPUTE AAA=100*Q55.
IF (Q56 NE 99) TOWNID=AAA+Q56.
IF (Q57 NE 99) TOWNID=AAA+Q57.
IF (Q58 NE 99) TOWNID=AAA+Q58.
IF (Q59 NE 99) TOWNID=AAA+Q59.
IF (Q60 NE 99) TOWNID=AAA+Q60.
IF (Q61 NE 99) TOWNID=AAA+Q61.
IF (Q62 NE 99) TOWNID=AAA+Q62.
IF (Q63 NE 99) TOWNID=AAA+Q63.
IF (Q64 NE 99) TOWNID=AAA+Q64.
IF (Q65 NE 99) TOWNID=AAA+Q65.
IF (Q66 NE 99) TOWNID=AAA+Q66.
IF (Q67 NE 99) TOWNID=AAA+Q67.
IF (Q68 NE 99) TOWNID=AAA+Q68.
IF (Q69 NE 99) TOWNID=AAA+Q69.
IF (Q70 NE 99) TOWNID=AAA+Q70.
IF (Q71 NE 99) TOWNID=AAA+Q71.
IF (Q72 NE 99) TOWNID=AAA+Q72.
IF (Q73 NE 99) TOWNID=AAA+Q73.
IF (Q74 NE 99) TOWNID=AAA+Q74.
IF (Q75 NE 99) TOWNID=AAA+Q75.                                                                                                
RECODE TOWNID (0=9999).                                                                          
COMPUTE AREAR=TOWNID.                                                                            
RECODE AREAR (201 THRU 299=7)
             (401 THRU 599=3) (700 THRU 899=4) (900 THRU 1099=5)                                 
             (1300 THRU 1399=6) (1400 THRU 1599=7) (1600 THRU 1699=6)                            
             (1700 THRU 1799=2) (1800 THRU 1899=3) (2000 THRU 2199=5) 
             (6300 THRU 6399=1) (6400 THRU 6499=6) 
             (6501 THRU 6506=1) (6507 THRU 6599=2)   
             (6600 THRU 6699=4) (6700 THRU 6799=5) (6800 THRU 6899=3)                     
             (ELSE=9).                                                                           
VARIABLE LABEL AREAR "地理區域(戶籍)".                                                                 
VALUE LABEL AREAR 1 "大臺北都會區" 2 "新北市基隆" 3 "桃竹苗" 4 "中彰投" 5 "雲嘉南"                 
                  6 "高屏澎" 7 "宜花東" 9 "無反應".                                              
fre AREAR.


*[建立統獨立場新變數].
compute TONDU=Q46.                                                                                                                                                  
recode TONDU (1 8=1)(2 7=6)(3=2)(4=5)(5=3)(6=4)(95 thru 99=9).                                                                                                            
var lab TONDU "統獨立場".                                                                                                                                             
val lab TONDU 1 "儘快統一" 2 "維持現狀，以後走向統一" 3 "維持現狀，看情形再決定獨立或統一" 4 "永遠維持現狀" 5 "維持現狀，以後走向獨立" 6 "儘快獨立" 9 "無反應".       
fre TONDU.
cro Q46 by TONDU.

*[建立台灣人/中國人認同新變數].
compute T_CIDENTITY=Q50.
recode T_CIDENTITY (95 96 97 98=9).
var lab T_CIDENTITY "台灣人/中國人認同".
val lab T_CIDENTITY 1 "台灣人" 2"都是" 3"中國人" 9"無反應".
fre T_CIDENTITY.
cro Q50 by T_CIDENTITY.


*[建立政黨認同新變數].                
compute PARTYID=0.                    
if (Q47=1) PARTYID=1.                 
if (Q47=6 and Q49=3) PARTYID=1.     
if (Q47=7 and Q49=3) PARTYID=1.    
if (Q47=10 and Q49=3) PARTYID=1.
if (Q47=16 and Q49=3) PARTYID=1.
if (Q47=18 and Q49=3) PARTYID=1.     
if (Q47=19 and Q49=3) PARTYID=1.     
if (Q47 gt 21 and Q49=3) PARTYID=1.  
if (Q47=2) PARTYID=2.     
if (Q47=6 and Q49=4) PARTYID=2.         
if (Q47=7 and Q49=4) PARTYID=2.   
if (Q47=8 and Q49=4) PARTYID=2.    
if (Q47=18 and Q49=4) PARTYID=2.    
if (Q47=19 and Q49=4) PARTYID=2.    
if (Q47 gt 21 and Q49=4) PARTYID=2.    
if (Q47=3) PARTYID=3.                 
if (Q47=6 and Q49=5) PARTYID=3.      
if (Q47=7 and Q49=5) PARTYID=3.   
if (Q47=9 and Q49=5) PARTYID=3.   
if (Q47=16 and Q49=5) PARTYID=3.   
if (Q47=18 and Q49=5) PARTYID=3.   
if (Q47=19 and Q49=5) PARTYID=3.   
if (Q47 gt 21 and Q49=5) PARTYID=3.    
if (Q47=4) PARTYID=4.                 
if (Q47=6 and Q49=6) PARTYID=4.     
if (Q47=7 and Q49=6) PARTYID=4.
if (Q47=18 and Q49=6) PARTYID=4.
if (Q47=19 and Q49=6) PARTYID=4.
if (Q47 gt 21 and Q49=6) PARTYID=4.    
if (Q47=5) PARTYID=5.  
if (Q47=6 and Q49=7) PARTYID=5.      
if (Q47=7 and Q49=7) PARTYID=5.      
if (Q47=18 and Q49=7) PARTYID=5.      
if (Q47=19 and Q49=7) PARTYID=5.      
if (Q47 gt 21 and Q49=7) PARTYID=5.   
if (Q47=21) PARTYID=6.  
if (Q47=6 and Q49=24) PARTYID=6.  
if (Q47=7 and Q49=24) PARTYID=6.  
if (Q47=18 and Q49=24) PARTYID=6.  
if (Q47=19 and Q49=24) PARTYID=6.  
if (Q47 gt 21 and Q49=24) PARTYID=6.     
if (Q47=38) PARTYID=7.
if (Q47=6 and Q49=41) PARTYID=7.
if (Q47=7 and Q49=41) PARTYID=7.
if (Q47=18 and Q49=41) PARTYID=7.
if (Q47=19 and Q49=41) PARTYID=7.
if (Q47 gt 21 and Q49=41) PARTYID=7.     
if ((Q47=6 or Q47=7 or Q47=16 or Q47=17 or Q47=18 or Q47=19  or Q47 gt 94) and (Q49=8 or Q49=18 or Q49=19 or Q49=20 or Q49=21 or Q49=96)) PARTYID=8. 
recode PARTYID(0=9).
var lab PARTYID "政黨認同".                                                                                        
val lab PARTYID 1 "國民黨" 2 "民進黨" 3 "新黨" 4 "親民黨" 5 "台灣團結聯盟" 6"時代力量" 7 "台灣民眾黨" 8 "中立及看情形" 9 "無反應及其他政黨".  
fre PARTYID.                                                                                                      
       
 
*政黨支持.
COMPUTE PARTY=0.                        
IF (Q47=1 AND Q48=1) PARTY=1.           
IF (Q47=1 AND Q48 GT 1) PARTY=2.        
IF (Q47 GT 5 AND Q49=3) PARTY=3.        
IF (Q47=2 AND Q48=1) PARTY=4.           
IF (Q47=2 AND Q48 GT 1) PARTY=5.        
IF (Q47 GT 5 AND Q49=4) PARTY=6.        
IF (Q47=3 AND Q48=1) PARTY=7.           
IF (Q47=3 AND Q48 GT 1) PARTY=8.        
IF (Q47 GT 5 AND Q49=5) PARTY=9.        
IF (Q47=4 AND Q48=1) PARTY=10.          
IF (Q47=4 AND Q48 GT 1) PARTY=11.       
IF (Q47 GT 5 AND Q49=6) PARTY=12.       
IF (Q47=5 AND Q48=1) PARTY=13.          
IF (Q47=5 AND Q48 GT 1) PARTY=14.       
IF (Q47 GT 5 AND Q49=7) PARTY=15.       
IF (Q47=21 AND Q48=1) PARTY=16.      
IF (Q47=21 AND Q48 GT 1) PARTY=17.     
IF (Q47 GT 5 AND Q49=24) PARTY=18.   
IF (Q47=38 AND Q48=1) PARTY=19.      
IF (Q47=38 AND Q48 GT 1) PARTY=20.     
IF (Q47 GT 5 AND Q49=41) PARTY=21.       
IF ((Q47=6 or Q47=7 or Q47=16 or Q47=17 or Q47=18 or Q47=19 or Q47=20 or Q47=23 or Q47=24) AND (Q49=8 or Q49=18 or Q49=19 or Q49=20 or Q49=21 or Q49=22 or Q49=23 or Q49=25)) PARTY=99.      
recode party(0=99).
VAR LAB PARTY "政黨支持".                                                                                 
val lab party 1 "非常支持國民黨" 2 "普通支持國民黨" 3 "偏國民黨" 4 "非常支持民進黨" 5 "普通支持民進黨" 6 "偏民進黨"          
              7 "非常支持新黨" 8 "普通支持新黨" 9 "偏新黨" 10 "非常支持親民黨" 11 "普通支持親民黨" 12 "偏親民黨"       
              13 "非常支持台聯" 14 "普通支持台聯" 15 "偏台聯"  16 "非常支持時代力量" 17 "普通支持時代力量" 18 "偏時代力量"
              19 "非常支持台灣民眾黨" 20 "普通支持台灣民眾黨" 21 "偏台灣民眾黨"  99 "中立無反應".
fre party.                                                                                                                   


*[原始併入變數].
VARIABLE LABELS BIRTH "出生年"
VARIABLE LABELS SENGI7 "父親省籍七分類".
VARIABLE LABELS MASENGI7 "母親省籍七分類".

VALUE LABELS  SENGI7
 1 "本省客家人"     2 "本省閩南人"   3 "大陸各省市人"    4 "原住民"     5 "外籍人士"      6 "大陸新住民"   7 "外國新住民"   9 "無反應".
VALUE LABELS  MASENGI7
 1 "本省客家人"     2 "本省閩南人"   3 "大陸各省市人"    4 "原住民"     5 "外籍人士"      6 "大陸新住民"   7 "外國新住民"   9 "無反應".


*[建立父親省籍新變數].
compute SENGI=SENGI7.
recode SENGI (1=1)(2=2)(3=3)(4=4)(ELSE=9).
var lab SENGI "父親省籍".
val lab SENGI 1 "本省客家人" 2 "本省閩南人" 3 "大陸各省市人" 4 "原住民"  9 "無反應、其他".
FRE SENGI.

*[建立母親省籍新變數].
compute MASENGI=MASENGI7.
recode MASENGI (1=1)(2=2)(3=3)(4=4)(ELSE=9).
var lab MASENGI "母親省籍".
val lab MASENGI 1 "本省客家人" 2 "本省閩南人" 3 "大陸各省市人" 4 "原住民"  9 "無反應、其他".
cro MASENGI7 by MASENGI.
FRE MASENGI.
