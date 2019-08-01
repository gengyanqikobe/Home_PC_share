import unittest
from Innotree.Auto.test_case.mxt import test_detail,test_analysis,test_search,test_trade


suite = unittest.TestSuite()

#企业查询接口:分别以产品，名称，标签搜索
#suggest接口:以名称，标签搜索
suite.addTest(test_search.Search('search_by_chanpin'))
suite.addTest(test_search.Search('search_by_biaoqian'))
suite.addTest(test_search.Search('search_by_name'))
suite.addTest(test_search.Search('suggest_by_biaoqian'))
suite.addTest(test_search.Search('suggest_by_name'))


#企业查询详情模块接口
suite.addTest(test_detail.Detail('detail_base'))
suite.addTest(test_detail.Detail('detail_teams'))
suite.addTest(test_detail.Detail('detail_patents'))
suite.addTest(test_detail.Detail('detail_competitions'))
suite.addTest(test_detail.Detail('detail_judgements'))
suite.addTest(test_detail.Detail('detail_tags'))
suite.addTest(test_detail.Detail('detail_finances'))

#企业画像/外贸信息模块接口
suite.addTest(test_analysis.Analysis('analysis_options'))
suite.addTest(test_analysis.Analysis('analysis_cate'))
suite.addTest(test_analysis.Analysis('analysis_country'))
suite.addTest(test_analysis.Analysis('trade_data'))


#贸易数据模块接口
suite.addTest(test_trade.Trade('trade_list_by_hs_area'))
#suite.addTest(test_trade.Trade('trade_export'))
suite.addTest(test_trade.Trade('trade_supplier_list'))


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)