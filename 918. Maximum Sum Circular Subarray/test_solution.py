import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySumCircular([1,-2,3,-2]), 3)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySumCircular([5,-3,5]), 10)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySumCircular([-3,-2,-3]), -2)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySumCircular([5]), 5)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySumCircular([-2]), -2)
    
    def test_case_6(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySumCircular([7050,-14105,-19820,-8590,28719,-29522,-17205,10602,-23749,-9148,-23122,-28050,28275,-18391,26527,-3777,-21166,-3960,22771,11655,-9048,-7202,-9025,22938,7696,-8750,-28043,6610,-13774,-5146,-21404,23006,-16012,-6692,16942,29758,-24041,-17420,-2920,-2661,-2603,9068,8885,-20897,28558,9782,-9982,-23296,4193,-29540,431,-22933,-28142,20558,-14822,17577,-6284,-1023,1493,-23348,-5700,21021,-2208,-354,-2323,-17867,15591,29632,18338,-29900,-204,16634,7771,27932,-28360,3564,14210,5950,-20765,-1317,22335,-13012,-1980,4220,-6016,-6777,-28811,2159,4932,7858,-16818,4195,-1374,11668,12430,2940,7614,9618,18859,-25514,-1786,13013,-6005,-15313,26391,-5438,2450,-29452,27467,-3527,-25903,26005,10459,18935,26883,-24888,15648,21154,-9095,5603,26138,-6387,692,29721,-29818,25879,-18057,-28409,-24345,-14612,-13544,25876,-23327,2212,6273,-8582,-23434,-28461,8799,11818,26056,-1186,16188,25526,-21041,-29468,3315,23719,-12181,-11558,-22232,2583,-9335,21404,-17528,19632,-1382,22235,9663,8849,-25155,-14733,6474,-25900,-14153,10399,2001,18764,4565,8776,22462,14897,-24648,-21245,-14279,-10603,26125,-24320,-20049,-5612,-16023,5449,15375,13891,20434,-28163,-20736,23307,-1600,270,-16559,-11115,-13566,-13853,-3262,-20682,-12866,4579,16847,-28467,-16365,25846,-1919,2901,-10860,-894,-7745,24589,-6104,-26906,9259,-25279,-26503,-12720,18912,23918,-16940,-27814,-7389,15520,17483,-16148,-28162,-15643,-9450,-20695,10099,12668,-17148,-8881,16419,-3639,5820,20070,-245,7789,12335,-4846,-3865,7615,27916,19618,-12505,14592,-10075,1936,-14852,-15074,-7188,-20723,-12627,-27644,510,28108,17066,21398,-26250,-11270,26355,4337,-2133,29763,28619,-29935,27934,-15396,10757,5566,-18463,28838,24580,-9834,-20987,-7123,-13430,24228,26262,11987,15263,-25506,14708,-18558,-23322,25286,5263,9375,-16573,23972,15746,29251,12436,-28486,-17973,7743,15789,-2981,-4858,2646,20454,23754,-2191,5951,-23590,-18357,19535,-6182,21801,-17118,-11008,23413,14298,-25163,21267,-27151,-4493,-29205,-4758,20363,1586,6641,28467,8417,12941,-5178,12089,-21711,16168,-22745,6932,-15543,17146,6508,-17201,5779,11555,15659,-26806,-7497,29879,1777,-25486,-3797,28909,-14132,-12471,-29273,-15530,-15206,19131,23631,29751,-7815,4877,-26397,14435,7941,14628,-21497,-8800,14109,-21962,16441,10127,-7455,-2580,28272,-6301,11811,20582,12996,5887,-8028,-6790,-7739,-26567,21257,-18232,11697,-9836,-1672,17574,-1716,2847,6040,7019,17556,-3831,17734,-24185,-15455,-25057,26275,27254,3252,-7896,295,-19965,-21310,3466,-20740,-19738,-341,-11593,-9097,29363,-9977,-11221,6955,24252,-2567,-12100,516,-12704,-9993,3345,12154,-5981,-12008,17196,-12232,-23183,28544,-11680,-15594,23871,-2785,-13757,26487,544,2972,17795,17297,-27297,13218,2055,-1194,660,29823,-17025,8965,-3126,13156,-4150,-24080,9974,-27090,29644,-8313,17347,-6610,7258,10979,28289,9536,-17537,21302,9932,-26900,693,-16781,15876,-11533,-20529,-20861,10003,-9981,28114,1498,29072,-28224,-24786,-20140,16147,-25472,-17776,10053,22288,-28870,-338,19358,-24726,-17049,18990,14656,-7588,-23024,-23383,-27416,10869,-22942,-29325,-29049,-15960,7251,27843,-16009,54,26793,19149,-7157,1425,25691,22284,23533,727,7297,-17918,-29319,18689,-15037,16867,4487,-3603,18087,14487,-15355,21684,28238,-17694,17900,-27786,18246,23941,-5034,1146,-21496,13116,4577,6638,-6265,22431,29146,16936,23174,-985,-28078,-28390,-21562,-10072,-8729,-925,-13518,20951,3118,24328,9153,18018,10359,3745,29389,-8958,-22950,23615,2092,3140,26741,19761,9225,-14416,20148,28364,-10583,-26378,17041,-20589,24691,2643,-6425,21821,16275,4910,-9182,-1881,19004,-28704,-8842,-17436,19418,10723,9531,-27200,-18576,-4256,-7056,2547,-2676,-28522,-7822,-29792,8612,-6811,-23534,10744,-24134,-18701,27708,23331,12530,-11388,-4922,28388,7119,13433,-6787,28644,5488,-16446,29764,8322,19390,-26243,20117,-21526,-15941,22763,-4969,25619,10883,29160,18935,18776,-881,-18613,-7134,11299,-392,27659,-20427,23163,-28992,-22023,-22161,-12287,-3945,12291,-28731,27124,5686,10710,16955,-17098,-20191,5249,-19036,-296,-13793,24357,-4794,3972,-7389,-25075,10697,10076,-16517,21772,7891,4309,25579,-24096,-10518,-18691,-3901,-24951,-21881,17814,-23099,223,28660,-23327,-19356,18556,-28712,1963,-11876,3494,9935,-29431,-20080,23769,8076,-17458,-25864,13600,21378,-16467,-28883,23449,-15920,-15187,-2383,10337,25793,28229,-19044,-9721,-5428,26400,-24408,-27109,25884,836,20956,-17628,-6554,-3765,10950,16638,8229,-18547,-5801,3412,292,4465,26804,-27686,-29972,-2971,-19970,16300,-14576,3768,21002,-15148,24538,27926,11603,6935,28944,4012,-128,24899,-24002,-27981,22342,-27068,-8747,-6031,1671,-8117,1985,17297,-9612,19104,-7350,26685,507,11146,6705,-11511,10003,19,25155,-13207,-7612,-2612,29376,-19056,-2837,-15296,-20351,-11045,2457,-13831,-9949,-1368,11288,15450,3507,-12038,-13343,15187,-18592,25540,12912,-18793,-18967,27854,8852,6382,13117,22004,-1094,13914,-1755,-28126,22123,-2764,27207,-25689,19788,-26322,24216,6753,-701,1028,-8614,-23936,9553,-28183,15704,17379,-14360,-26528,-29259,24852,-2124,-7499,20276,-27803,-12004,-7811,18942,9470,-20837,7248,-9541,-1216,-14841,22389,-2630,5268,-4443,11060,-24016,-7253,8332,6,-17363,-1843,29207,25671,-21687,23916,-9221,12511,-12629,27008,20285,14705,7936,20703,7884,21069,9878,-20102,14386,9043,-19089,-12909,10864,-5744,-13966,-10739,17395,-17851,3806,26063,-1607,4721,409,18764,-14353,-28166,13043,13750,28554,-21303,1350,-15676,-6532,-27252,29065,-22392,14939,22006,-22960,-653,21794,-29890,16587,-11510,-2925,-29606,6926,20230,-28030,-12333,-25022,25431,-27156,-27754,-11043,18144,-540,-10870,-14975,-8860,8988,-21875,-27837,1667,-9164,-17990,-20919,9189,10977,-16005,-2947,-16406,-13756,-28163,-15153,14707,-15397,10188,1809,17798,8912,-8218,-19331,-5043,-20219,-6187,-4799,-29307,5452,-23324,-407,-9211,268,-23495,966,-6598,19895,-27681,-25792,-13709,27991,-18029,-27088,25054,20893,15162,2953,24149,14956,-17416,9773,-3341,-12603,2655,-4602,8579,-21549,17593,1122,20859,-2932,27401,-14384,11022,-19044,-7038,-307,-7248,10763,22889,-25555,12470,-4504,-694,-12214,10609,-29208,21964,-27391,193,19108,-6130,-27211,2484,27361,-292,24642,-20912,-8074,-16921,16150,-20182,15650,10111,10112,16845,21941,-14314,7370,-14715,2714,19894,-21419,2958,-19226,29247,-521,15346,-1678,29630,-3766,1186,-23461,-639,-29865,28910,-17502,29551,-900,16183,1354,10049,-24360,29791,22399,26394,1193,-15855,29296,-9978,-9116,23229,19583,-14667,-15587,3966,10242,11608,15050,-23906,-3143,-14586,-17342,28954,11362,-17216,-22445,26089,-8551,-665,18248,-6788,22307,-15444,22027,1272,22318,-15445,9995,4804,19798,24063,-19959,12217,-20698,-12770,-7506,-6014,-6856,-2470,-19440,-21035,8123,-26390,-27899,385,10529,-7621,12082,-28277,-336,-26239,15522,14705,-15028,18543,9004,-25327,-27240,824,18380,3626,2070,-21410,8501,-2748,-25870,13514,21461,17949,12772,-24205,-8839,21793,-6207,-8580,-8977,18853,3228,-22909,-3695,-1325,26246,-22394,26655,-19834,22415,-9534,2799,10034,15579,-112,5388,11600,21186,-11818,-10801,28384,22834,-19472,-11652,-24711,24901,10996,25988,3059,9921,-21759,29489,22828,-23066,-9678,-14718,11608,8025,-3773,14468,-24925,-12529,-24085,-15123,28804,-4027,-13186,-4151,-15525,-16266,1210,834,-13747,17778,-2408,-22962,-1289,19038,-16490,-22180,-8305,-4242,-12944,-6913,-28104,29546,-19237,-23678,1770,-1142,-22314,11961,392,-11642,-19716,26051,-21946,24059,22573,15781,24362,9955,-24088,-9667,23349,2005,-18604,-7122,26367,9778,-4446,16155,7100,12477,-16250,-6638,-15594,29133,892,-963,12499,-24451,-13101,15979,-20765,27915,-13397,12581,25368,-24799,-11161,-15805,8120,-737,5679,22088,-8581,8421,-26147,14434,-24838,2034,-20487,19589,-7225,24602,-9243,29254,-16185,10554,-12534,26477,-12136,-27873,8356,-25519,-14443,9797,-22267,-24458,9168,-10599,-6396,-7004,16161,-19749,-26721,12591,25837,12702,-21389,9367,-18061,-3108,1324,24376,-741,12679,5147,15156,-17658,-15000,16940,21787,4324,13309,-2020,-9937,-15363,-13190,29745,-27410,13268,-5363,-15114,-13012,-10236,7853,23258,10833,17272,25245,-19297,-8002,-29620,-16783,19629,-21019,4138,-23692,28813,21788,22470,-2294,28338,2779,28346,7517,-8787,13355,-29519,3198,-7182,-13774,-24106,-13489,-21276,21032,-10709,-26029,26072,15222,-13865,-220,14385,19121,-426,15283,14572,-11220,4415,-18371,5040,19857,-20098,28391,26386,-28650,-25454,2318,16305,-12753,7906,27038,14422,-26310,-11903,24962,4748,29474,-3668,22322,-29816,-4373,-675,20607,26299,-2944,17028,2665,8608,-16074,15158,-28025,-6691,-24575,-6960,-12553,3445,23852,-8862,17588,-1919,-23608,-20235,-21791,4868,-3045,-19426,2926,-17728,28159,5102,22402,-24867,-12046,13602,-4323,-1539,-2755,8733,-20718,5236,15921,-29845,-28833,15015,710,-2258,4065,-19915,-11707,-6207,-20517,21333,-22996,23745,-28759,21221,-20256,2089,26895,-16177,2356,-4203,-7366,7089,-1399,678,26160,13331,3375,-9804,-12392,-27364,6918,-26367,-14981,-29169,6718,-27996,-26425,27255,-18891,-11667,-26296,19856,-10237,-14763,-20768,17339,-21388,-8594,-18673,26617,-6957,23341,-13408,13194,19173,-28459,-26421,10312,-19317,16685,-21710,-15313,-19850,16648,23288,29314,-24992,-20307,13333,16530,17915,14803,-13682,2078,16233,-17612,-29469,16145,19912,25957,17725,29192,12970,26387,6471,25755,-11953,19907,-9707,29183,21489,-5907,-26051,-19362,2998,-24382,481,-12657,17236,-13268,-23176,1182,-29749,23462,1974,8609,-20845,27893,-19140,29481,-10790,4507,4738,-9245,5999,-29068,-3470,-27112,11978,10041,-12681,28883,-28518,25738,15935,-14050,24501,-8392,-14390,29687,-22435,19458,-20195,15065,17255,10001,-12715,-9704,-26620,15801,12114,5297,8053,15018,16193,-536,19580,19222,-17077,-826,5910,29560,10890,24639,24844,2737,24152,-12229,-15349,6663,22281,4623,-28989,-6655,-11996,-26336,11875,17992,20001,-29472,22830,-25595,20855,22596,27404,-2701,28339,11073,-11416,-23356,2025,16186,18487,19960,-1118,-29954,4154,-8424,-982,18747,15225,25855,-19847,-1941,17906,-1741,-16759,9612,-26304,17495,-4355,16096,11654,18932,-18523,-19937,28524,-17196,16819,19426,9921,-19400,-21376,-4295,-7864,496,4120,-2121,21114,21889,-8123,2768,1995,-5300,-27048,-18578,24089,-13743,17906,-26254,9653,-3587,-11384,19251,-5347,21155,-23359,11310,-27020,29336,14700,-3921,13572,-4516,7522,-14561,-20982,-28617,4627,-15826,-12873,-15130,19990,-7239,18735,8751,-5160,25403,10046,-21901,-27280,29655,19310,-16306,-23590,-20257,-27924,-20573,-26821,-6075,-2514,5240,15685,-29432,-27032,-155,-5722,-3450,29578,-24750,4435,-14200,13564,-17435,13164,-382,-5778,12328,-16898,-10948,-9239,16692,26588,11352,28954,20939,20279,-19217,-21403,2007,3204,13116,-27171,-8199,-11409,25760,25513,22392,253,20974,9555,-6157,16113,13833,-4594,4372,-4293,17714,26701,-27358,8551,-29306,-18918,1587,13843,21708,-26197,3957,19160,22994,7781,-21855,-24070,14470,11311,-10847,20556,-9250,-10993,22155,-6626,-21986,20711,-8476,28985,20574,-5528,22360,22178,6459,-12884,28331,-25678,3528,-6895,-4209,25373,24035,-10522,-5389,-11712,22457,27008,-3256,16272,22171,13048,-9564,-7136,-24176,-8321,-29604,28698,25743,28272,1935,-13088,-3581,5849,-14,-352,16076,1417,16100,27049,19483,1088,-5256,22762,2295,22325,29821,-9947,-19788,-26880,-7669,11765,15047,2574,-7632,-1567,1452,5989,-10015,13541,-19528,11545,19608,-14714,21664,-2893,-29530,-23589,-22916,28673,-13967,13872,-14451,-14617,18118,-10940,-10346,2823,25157,-20908,-23594,-19894,-7676,-12626,-23660,-14994,7353,28329,3860,-13301,-2819,23088,18344,10375,-11156,17055,-21379,-22824,25510,8905,10550,-29343,-267,-21332,21033,2508,20532,16845,-29785,-19008,21467,23965,-29930,-18166,-14590,5693,4190,-23678,22874,-10456,5126,15745,-23426,-6102,-20073,920,-2736,-2870,-2270,19893,21260,-25267,-2480,2381,25219,-29233,-23591,6479,-14795,-24161,28625,-10759,-23491,15947,-9316,18963,16697,14935,10063,-19706,-25410,-28839,10392,6845,26639,8212,-24373,-22087,-12367,-8634,29524,4038,-13353,-19182,-16231,1621,1797,-25590,-28804,316,-4946,11653,15169,4597,-8212,-2853,575,448,18313,18703,873,-15046,-23667,-21903,11315,-1669,-5323,6205,25651,-385,-28528,21823,-18654,17204,15639,-24061,9501,25919,-872,-10555,-975,-14972,6159,7620,-20180,-20946,21763,2762,3253,-23641,13008,8182,21134,-24511,-21494,-16231,23590,29519,-12846,-29905,11657,6107,-2060,-25696,27343,28566,11244,-24131,5357,20039,10348,24068,-29703,-7828,10583,29452,-5766,7251,-19828,14190,25186,-20182,29099,14537,25722,18614,-28884,-24963,-24483,14312,-26468,-4550,-10384,-13901,-4320,-5029,-24974,-9896,6347,-1812,-22673,15109,21289,22431,9498,11572,-9399,27052,28941,11388,13100,20791,19718,16940,-22387,1416,-4485,8142,-12380,17529,-11899,4077,27993,11249,-6369,-8407,-1271,-2729,20425,-16046,17140,-20271,-18119,11182,20983,-3377,25604,17549,-19135,-4475,-28164,-2435,29290,2013,8313,7854,-8294,-25719,23478,-8476,-15280,-14682,29199,-2160,-1714,-23820,7106,-5555,18960,-12153,3169,-14138,25893,-20705,28541,-2956,-17419,-29869,-3556,13274,21071,21801,17840,-8522,2179,2704,-27085,1408,20120,-8189,-15742,20657,-16186,900,-13413,-12459,-14473,-4560,-13183,18298,-26857,27981,-12543,19953,-4404,-15313,101,-6975,-9046,6534,1471,2788,-18211,-4596,7034,-12503,-3258,-26779,-15375,18649,-365,-10868,19578,-3293,6696,-16377,3207,261,-9495,-9352,21900,21183,10134,21591,9969,-4599,7742,-3232,15145,28052,12005,-10723,420,-28787,25224,15847,-5880,-5487,3089,-25574,-19599,-13696,6920,17610,5553,29741,10323,11930,-6943,-15486,-22817,-7970,-20931,6490,-3073,-7197,15090,16418,24418,-3216,-11905,19268,-24579,-2838,-24744,9379,11067,24822,17411,-17715,-23373,4346,-15575,-21348,-19023,-12830,10153,1542,12282,5891,5787,-5036,15685,-9690,19644,23355,-9027,15346,4785,2089,-16195,25646,-3764,10587,-22533,-10189,17909,10143,26681,-26406,-2837,-14297,21904,8037,6788,631,-29789,29528,6246,-7835,-26459,28506,14483,11854,14470,-4066,9697,-16207,-13657,-6576,18188,-28770,8502,24000,-12033,21547,21870,3056,-28205,-21251,19089,-4485,-5063,-7459,-23185,-6488,-8377,-22108,17546,15036,28985,-15270,-19316,-16716,16442,-20692,1221,17923,5179,7847,-23763,-21538,-11130,26466,14772,9757,-11802,-9347,-4342,18713,28951,28386,11126,-19455,-21121,-29231,-10054,3718,-7727,26863,-11526,29022,-20075,-1717,-4413,-16938,-25463,-2806,115,-15604,-948,19942,1152,13743,-28631,-21508,10791,-21059,6713,3420,-19138,-17964,16654,29016,28315,-27337,17975,-15759,12467,-16233,-3267,-28300,10398,-4743,-16051,-6673,14819,-22891,-29860,28236,13234,22929,-17022,29957,-10554,-9829,16996,12818,26956,11473,18872,-11260,19394,-26619,-29704,15252,-18062,-18564,12459,-3078,18384,-18756,-118,-9798,8548,-3138,1074,-6259,9371,12986,25484,-21141,3192,-3729,23785,4945,-13080,-11169,-18908,10232,-23037,3852,-18075,-3357,-13895,-5594,-29314,-6603,-8484,2672,-17568,-26311,-23649,-25776,-7221,5299,-23615,-18049,-14629,8859,25853,27585,-9267,-22053,14477,-2697,15258,-28768,-21733,-692,3801,-21952,2659,-27462,-25138,27508,27214,-29433,-16051,3391,7476,-12443,2373,12406,930,1800,-26043,-26242,-3112,-11943,-26785,-2929,8819,-24024,-28419,-12735,18239,-13096,11295,-17057,-4046,-26152,-14881,-9639,-17075,-13020,11304,13305,27141,17535,-19645,-23088,-22664,8527,22536,-19915,1148,-11724,-18483,-5071,22594,-1010,26758,1585,7752,-17527,-28350,-22377,-6773,369,-26886,11534,-3687,27255,-25608,7359,-633,26339,27935,-29665,23141,16808,-19651,-20253,587,25014,-19643,19003,-3215,-12921,17188,4216,-19261,19522,29292,-1513,-14770,-1967,2452,28585,-15986,1761,14967,-19626,4624,-4887,-16302,-28671,-5810,10770,19782,-21965,-26201,23670,-16648,-27486,781,26722,8510,13425,4011,-11080,12289,-455,-28375,22503,-13136,10525,-5738,-26662,13717,28064,17376,8475,26907,18174,28450,11518,26018,11820,8568,2664,22628,-27789,-8446,-19731,19379,-29896,3620,-561,-26440,23344,-6843,13540,23081,17177,23133,7420,-20757,-28554,-12765,2374,-1896,19499,2239,8951,8481,-14960,-2308,-24733,-4705,8373,10346,-4803,-538,25918,13043,14474,-20866,13756,17465,-4536,-14234,-21835,3126,21654,9963,27292,-20394,-12616,-14262,23968,-7880,-6462,-3873,-1744,1669,-457,-11445,-29561,-7761,5383,2964,25373,2160,-12191,-12802,16873,-25532,14865,-20272,836,8374,2022,-7517,12893,-5592,-12180,-8925,-28004,-23180,-83,-29301,-16870,29144,-23896,18909,-26351,20373,-28488,7311,13969,9232,-17712,28629,-16109,-20136,-15503,-3430,14089,16499,462,1206,19627,23144,-24021,-29115,9213,14879,-7193,-4291,24615,-8491,24749,26352,-8167,-26707,-4741,-28089,16475,-22577,20082,2045,-13194,22598,13188,-3091,-2266,-21825,26888,24562,27925,-12923,-8663,-15573,-1834,-22613,21205,-26819,656,29012,28498,27723,6145,-9790,-18381,-11689,-26548,1547,13783,-4103,4466,-19604,27633,-6866,-1034,13275,-11577,1898,20511,2920,3994,16715,27687,-15590,-22276,-2910,-12043,-7550,7416,26296,-29900,-20759,23645,-20773,13812,-20086,-16938,-25484,-25762,2657,-22843,-6385,-8759,15464,14382,43,-20655,11575,-10067,-7362,232,-5927,22134,-3652,-15829,6872,8096,19344,-2914,-2367,26207,23973,3089,-21069,3928,-18340,-21438,-16530,28099,8304,27776,-13447,18915,-16997,-28487,-4393,-13192,27917,17483,-12774,12097,23458,-2253,12335,-19299,29123,19313,2266,-592,19059,-7490,-20963,-11010,3090,15750,-2895,4032,4432,-4417,-26669,26270,18427,-10506,-11500,9297,-2945,10603,17387,26599,3338,-18312,19450,-11681,-18332,-12833,135,14832,-23498,-26519,-29791,-26201,-12861,11293,29892,-17307,16202,-7743,22894,-23650,2734,-8725,-18842,-11279,-10761,-29811,-8801,13529,-16968,-6556,-8572,25859,-25835,-7153,19395,-18544,7068,27455,-20949,29315,20005,1871,11577,5142,5912,-24225,7208,14828,-6987,-23341,3314,-10849,-6204,28146,1934,12052,-19083,-20464,-25784,9533,26290,-20089,9467,-28399,-28353,-3211,-1084,1056,25741,17776,11566,16247,12851,-25247,25989,-10011,3646,9961,-23157,4239,22201,11683,-24840,15630,-17304,-8728,-26476,2427,21332,-4087,-8236,9862,17899,3890,4167,13857,-3353,-28922,13403,6701,27776,1437,-7585,-25538,-19609,25796,-7862,17235,11883,-1766,-13223,-21773,26990,-26650,5095,-19026,-26304,5759,-16369,12430,25652,17834,-1724,-28731,-18608,16675,2040,19590,-4870,-27580,-15186,-3672,11972,29868,23081,-907,-8687,18497,-27475,-6280,4856,-4466,-17306,-5193,-12422,-15525,1095,27650,-11646,9711,14338,29826,-25941,-3508,5313,7630,26699,18003,3400,-26192,-18689,10426,-3176,-19940,17148,23166,-29189,19429,-7168,-3899,28282,4230,11943,-27157,4067,15667,29376,-24571,11847,28099,15648,5254,15846,836,27900,13934,-23031,24714,8383,-29014,22288,26758,-15304,-21652,26184,-9803,-17979,-7579,-12430,17172,-26594,-16516,-4671,-23362,-12299,-21772,-21834,24747,22743,-17774,-28079,768,-10484,6315,-23929,-28121,22059,28672,-8117,-6435,21598,26359,15880,908,1789,9284,23786,28837,-12291,-18179,9121,14347,7007,-20336,-6552,-16388,-28751,25529,-24059,-455,26219,-16899,9339,-19263,-13770,-3717]), 805043)