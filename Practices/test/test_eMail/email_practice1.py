




import smtplib
from email.mime.text import MIMEText    #发送邮件要填充的成员
from  email.header import Header        #设置编码格式
import datetime
import string


dt = datetime.datetime.now()
str_time = dt.strftime('%y-%m-%d %H:%M:%S') #用于标题栏的发送时间和日期

#发送方邮件地址

sender = 'gengyanqikobe@163.com'

#发送方的授权码，不是密码

pwd = 'shouquanma1'

receivers = ['yanqi.geng@innotree.cn','1321188988@qq.com']

#邮件的内容，收件人，发件人信息


# mail_message = '<html><body><h1>Hello</h1>' + \
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
#     '</body></html>'

mail_message = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Test Report</title>
    <meta name="author" content="Oleksii Skliarov, Ivan Lysenko"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <style type="text/css" media="screen">
        body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
        table       { font-size: 100%; }
        pre         { }

        /* -- heading ---------------------------------------------------------------------- */
        h1 {
            font-size: 16pt;
            color: gray;
        }
        .heading {
            margin-top: 0ex;
            margin-bottom: 1ex;
        }

        .heading .attribute {
            margin-top: 1ex;
            margin-bottom: 0;
        }

        .heading .description {
            margin-top: 4ex;
            margin-bottom: 6ex;
        }

        /* -- css div popup ------------------------------------------------------------------------ */
        a.popup_link {
        }

        a.popup_link:hover {
            color: red;
        }

        .popup_window {
            display: none;
            position: relative;
            left: 0px;
            top: 0px;
            /*border: solid #627173 1px; */
            padding: 8px;
            background-color: #E6E6D6;
            font-family: "Lucida Console", "Courier New", Courier, monospace;
            text-align: left;
            font-size: 8pt;
            width: 570px;
        }

        }
        /* -- report ------------------------------------------------------------------------ */
        #show_detail_line {
            margin-top: 3ex;
            margin-bottom: 1ex;
        }
        .result_table {
            width: 80%;
            border-collapse: collapse;
            border: 1px solid #777;
        }
        #header_row {
            font-weight: bold;
            color: white;
            background-color: #777;
        }
        .result_table td {
            border: 1px solid #777;
            padding: 2px;
        }
        .shortDescription {
            font-style: italic;
            font-weight: normal;
        }
        #total_row  { font-weight: bold; }
        .passClass  { background-color: #6c6; }
        .failClass  { background-color: #c60; }
        .errorClass { background-color: #c00; }
        .passCase   { color: #6c6; }
        .failCase   { color: #c60; font-weight: bold; }
        .errorCase  { color: #c00; font-weight: bold; }
        .hiddenRow  { display: none; }

        .testcase   { display: none; }
		.testclass.active ~ .testcase { display: table-row; }

        /* -- ending ---------------------------------------------------------------------- */
        #ending {
        }

    </style>
</head>
<body>
<script language="javascript" type="text/javascript">
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByClassName("testclass");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        if(0==level && tr.className.indexOf("active") != -1){
			tr.className = tr.className.replace("active", "").replace("  ", " ").trim();
		}else if (2 == level && tr.className.indexOf("active") == -1){
			tr.className+=" active";
		}else if (1 == level){
			if(tr.className.indexOf("passClass") != -1){
				if(tr.className.indexOf("active") != -1){
					tr.className = tr.className.replace("active", "").replace("  ", " ").trim();
				}
			}else if (tr.className.indexOf("active") == -1){
				tr.className+=" active";
			}
        }
    }
}

function showClassDetail(element) {
    var currentClassValue = element.className || "";

    if (currentClassValue.indexOf("active") == -1) {
		currentClassValue += " active";
    } else {
		currentClassValue = currentClassValue.replace("active", "").replace("  ", " ");
	}
	element.className = currentClassValue.trim();
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}

function togleClass(element, clas){
        var currentClassValue = element.className || "";

        if (currentClassValue.indexOf(clas) == -1) {
            currentClassValue += " "+clas;
        } else {
            currentClassValue = currentClassValue.replace(clas, "").replace("  ", " ");
        }
        element.className = currentClassValue.trim()
    }

function showRawLog(element){
        togleClass(element, "popup_window")
    }

function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

</script>

<table>
    <tr id="header_row">
        <th>Class</th>
        <th>Fail</th>
        <th>Error</th>
        <th>Skip</th>
        <th>Success</th>
        <th>Total</th><p align='center'> <font size='5'><a href='http://172.28.102.148:2500/innotreetest/home'>返回主页</a></font> </p>
    </tr>
        <tr>
            <td>城市产业服务平台_首页区域概览</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>官网-登录接口</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>开放平台-机构搜索-关键字金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>开放平台-公司搜索-关键字金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>官网-公司搜索-标签金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>官网-首页加载</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>贸信通(用户端)-搜索</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>贸信通_基本信息</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>2</td>
            <td>2</td>
        </tr>
        <tr>
            <td>开放平台-公司详情-基本信息</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>官网-公司详情</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>BI(O)对外-机构搜索-标签金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>BI(O)对外-机构搜索-关键字金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>BI(O)对外-人才搜索-王</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>贸信通_企业画像_区域分析</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>开放平台-机构搜索-标签金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>城市产业服务平台_产业分析</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>3</td>
            <td>3</td>
        </tr>
        <tr>
            <td>贸信通(审核端)-综合查看-基础认证企业查询</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>开放平台-公司搜索-标签金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>开放平台-机构详情-基本信息</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>贸信通_企业图谱</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>官网-公司搜索-关键字金融</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>开放平台-公司详情-公司标签</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
    <tr>
        <td><strong>Total</strong></td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>24</td>
        <td>25</td>
    </tr>
</table>

<!-- test list -->
<!-- header -->
<p id='show_detail_line'>Show
<a href='javascript:showCase(0)'>Summary</a>
<a href='javascript:showCase(1)'>Failed</a>
<a href='javascript:showCase(2)'>All</a>
</p>
<table class='result_table'>
    <colgroup>
        <col align='left' width="50%" />
        <col align='right' width="10%"/>
        <col align='right' width="10%"/>
        <col align='right' width="10%"/>
        <col align='right' width="10%"/>
        <col align='right' width="10%"/>
    </colgroup>
    <tr id='header_row'>
        <td>Test Group/Test case 2019-04-28 04:06:02</td>
        <td>Count</td>
        <td>Pass</td>
        <td>Fail</td>
        <td>Error</td>
        <td>View</td>
    </tr>
</table>
<!-- for every test suite -->
    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>城市产业服务平台_首页区域概览</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='城市产业服务平台_首页区域概览test_cityServiceHome' class='testcase'>
            <td class="passCase">
                test_cityServiceHome
            </td>
            <td>0:00:00.029565</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_城市产业服务平台_首页区域概览test_cityServiceHome')" >
                Pass
            </a>

            <div id='div_城市产业服务平台_首页区域概览test_cityServiceHome' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_城市产业服务平台_首页区域概览test_cityServiceHome').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>官网-登录接口</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='官网-登录接口test_add_url' class='testcase'>
            <td class="passCase">
                test_add_url
            </td>
            <td>0:00:00.046492</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_官网-登录接口test_add_url')" >
                Pass
            </a>

            <div id='div_官网-登录接口test_add_url' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_官网-登录接口test_add_url').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>开放平台-机构搜索-关键字金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-机构搜索-关键字金融test_instNum' class='testcase'>
            <td class="passCase">
                test_instNum
            </td>
            <td>0:00:00.066071</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-机构搜索-关键字金融test_instNum')" >
                Pass
            </a>

            <div id='div_开放平台-机构搜索-关键字金融test_instNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-机构搜索-关键字金融test_instNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>{"keywords": "\u91d1\u878d", "type": "1", "andOr": "1"}



                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>开放平台-公司搜索-关键字金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-公司搜索-关键字金融test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.090473</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-公司搜索-关键字金融test_corpNum')" >
                Pass
            </a>

            <div id='div_开放平台-公司搜索-关键字金融test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-公司搜索-关键字金融test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>官网-公司搜索-标签金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='官网-公司搜索-标签金融test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.080373</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_官网-公司搜索-标签金融test_corpNum')" >
                Pass
            </a>

            <div id='div_官网-公司搜索-标签金融test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_官网-公司搜索-标签金融test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>官网-首页加载</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='官网-首页加载test_innotree_index' class='testcase'>
            <td class="passCase">
                test_innotree_index
            </td>
            <td>0:00:00.063573</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_官网-首页加载test_innotree_index')" >
                Pass
            </a>

            <div id='div_官网-首页加载test_innotree_index' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_官网-首页加载test_innotree_index').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>贸信通(用户端)-搜索</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='贸信通(用户端)-搜索test_mxtCrop' class='testcase'>
            <td class="passCase">
                test_mxtCrop
            </td>
            <td>0:00:01.981879</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_贸信通(用户端)-搜索test_mxtCrop')" >
                Pass
            </a>

            <div id='div_贸信通(用户端)-搜索test_mxtCrop' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_贸信通(用户端)-搜索test_mxtCrop').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>32766269



                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>贸信通_基本信息</td>
            <td>2</td>
            <td>2</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='贸信通_基本信息test_mxtDetailBase' class='testcase'>
            <td class="passCase">
                test_mxtDetailBase
            </td>
            <td>0:00:00.083829</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_贸信通_基本信息test_mxtDetailBase')" >
                Pass
            </a>

            <div id='div_贸信通_基本信息test_mxtDetailBase' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_贸信通_基本信息test_mxtDetailBase').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>
<tr id='贸信通_基本信息test_mxtDetailTupu' class='testcase'>
            <td class="passCase">
                test_mxtDetailTupu
            </td>
            <td>0:00:00.053520</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_贸信通_基本信息test_mxtDetailTupu')" >
                Pass
            </a>

            <div id='div_贸信通_基本信息test_mxtDetailTupu' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_贸信通_基本信息test_mxtDetailTupu').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>开放平台-公司详情-基本信息</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-公司详情-基本信息test_base' class='testcase'>
            <td class="passCase">
                test_base
            </td>
            <td>0:00:00.022055</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-公司详情-基本信息test_base')" >
                Pass
            </a>

            <div id='div_开放平台-公司详情-基本信息test_base' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-公司详情-基本信息test_base').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>官网-公司详情</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='官网-公司详情test_innoCrop_detail' class='testcase'>
            <td class="passCase">
                test_innoCrop_detail
            </td>
            <td>0:00:00.058007</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_官网-公司详情test_innoCrop_detail')" >
                Pass
            </a>

            <div id='div_官网-公司详情test_innoCrop_detail' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_官网-公司详情test_innoCrop_detail').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>BI(O)对外-机构搜索-标签金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='BI(O)对外-机构搜索-标签金融test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.367343</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_BI(O)对外-机构搜索-标签金融test_corpNum')" >
                Pass
            </a>

            <div id='div_BI(O)对外-机构搜索-标签金融test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_BI(O)对外-机构搜索-标签金融test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>BI(O)对外-机构搜索-关键字金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='BI(O)对外-机构搜索-关键字金融test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.072147</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_BI(O)对外-机构搜索-关键字金融test_corpNum')" >
                Pass
            </a>

            <div id='div_BI(O)对外-机构搜索-关键字金融test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_BI(O)对外-机构搜索-关键字金融test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>BI(O)对外-人才搜索-王</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='BI(O)对外-人才搜索-王test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.055133</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_BI(O)对外-人才搜索-王test_corpNum')" >
                Pass
            </a>

            <div id='div_BI(O)对外-人才搜索-王test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_BI(O)对外-人才搜索-王test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>贸信通_企业画像_区域分析</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='贸信通_企业画像_区域分析test_mxtHuax' class='testcase'>
            <td class="passCase">
                test_mxtHuax
            </td>
            <td>0:00:00.107920</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_贸信通_企业画像_区域分析test_mxtHuax')" >
                Pass
            </a>

            <div id='div_贸信通_企业画像_区域分析test_mxtHuax' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_贸信通_企业画像_区域分析test_mxtHuax').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>开放平台-机构搜索-标签金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-机构搜索-标签金融test_instNum' class='testcase'>
            <td class="passCase">
                test_instNum
            </td>
            <td>0:00:00.417639</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-机构搜索-标签金融test_instNum')" >
                Pass
            </a>

            <div id='div_开放平台-机构搜索-标签金融test_instNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-机构搜索-标签金融test_instNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>城市产业服务平台_产业分析</td>
            <td>3</td>
            <td>3</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='城市产业服务平台_产业分析test_cityServiceComp' class='testcase'>
            <td class="passCase">
                test_cityServiceComp
            </td>
            <td>0:00:00.043765</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_城市产业服务平台_产业分析test_cityServiceComp')" >
                Pass
            </a>

            <div id='div_城市产业服务平台_产业分析test_cityServiceComp' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_城市产业服务平台_产业分析test_cityServiceComp').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>
<tr id='城市产业服务平台_产业分析test_cityServiceJishu' class='testcase'>
            <td class="passCase">
                test_cityServiceJishu
            </td>
            <td>0:00:00.042244</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_城市产业服务平台_产业分析test_cityServiceJishu')" >
                Pass
            </a>

            <div id='div_城市产业服务平台_产业分析test_cityServiceJishu' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_城市产业服务平台_产业分析test_cityServiceJishu').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>
<tr id='城市产业服务平台_产业分析test_cityServiceZijin' class='testcase'>
            <td class="passCase">
                test_cityServiceZijin
            </td>
            <td>0:00:00.020911</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_城市产业服务平台_产业分析test_cityServiceZijin')" >
                Pass
            </a>

            <div id='div_城市产业服务平台_产业分析test_cityServiceZijin' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_城市产业服务平台_产业分析test_cityServiceZijin').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>贸信通(审核端)-综合查看-基础认证企业查询</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='贸信通(审核端)-综合查看-基础认证企业查询test_mxtJcQuery' class='testcase'>
            <td class="passCase">
                test_mxtJcQuery
            </td>
            <td>0:00:00.185895</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_贸信通(审核端)-综合查看-基础认证企业查询test_mxtJcQuery')" >
                Pass
            </a>

            <div id='div_贸信通(审核端)-综合查看-基础认证企业查询test_mxtJcQuery' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_贸信通(审核端)-综合查看-基础认证企业查询test_mxtJcQuery').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>开放平台-公司搜索-标签金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-公司搜索-标签金融test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.191777</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-公司搜索-标签金融test_corpNum')" >
                Pass
            </a>

            <div id='div_开放平台-公司搜索-标签金融test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-公司搜索-标签金融test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>开放平台-机构详情-基本信息</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-机构详情-基本信息test_base' class='testcase'>
            <td class="passCase">
                test_base
            </td>
            <td>0:00:00.031743</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-机构详情-基本信息test_base')" >
                Pass
            </a>

            <div id='div_开放平台-机构详情-基本信息test_base' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-机构详情-基本信息test_base').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>贸信通_企业图谱</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='贸信通_企业图谱test_mxtCompTupu' class='testcase'>
            <td class="passCase">
                test_mxtCompTupu
            </td>
            <td>0:00:00.115240</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_贸信通_企业图谱test_mxtCompTupu')" >
                Pass
            </a>

            <div id='div_贸信通_企业图谱test_mxtCompTupu' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_贸信通_企业图谱test_mxtCompTupu').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>2



                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass passClass'>
            <td>官网-公司搜索-关键字金融</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='官网-公司搜索-关键字金融test_corpNum' class='testcase'>
            <td class="passCase">
                test_corpNum
            </td>
            <td>0:00:00.133118</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_官网-公司搜索-关键字金融test_corpNum')" >
                Pass
            </a>

            <div id='div_官网-公司搜索-关键字金融test_corpNum' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_官网-公司搜索-关键字金融test_corpNum').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>


                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr>    <table class='result_table'>
	    <colgroup>
            <col align='left' width="50%" />
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
            <col align='right' width="10%"/>
        </colgroup>
        <tr class='testclass failClass'>
            <td>开放平台-公司详情-公司标签</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
            <td>0</td>
            <td><a href="javascript:void(0)" onclick="showClassDetail(this.parentNode.parentNode)">Detail</a></td>
        </tr>
        <!-- for every test -->

<tr id='开放平台-公司详情-公司标签test_tag' class='testcase'>
            <td class="failCase">
                test_tag
            </td>
            <td>0:00:00.021744</td>
            <td colspan='4' align='center'>
            <!--css div popup start-->
            <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_开放平台-公司详情-公司标签test_tag')" >
                Fail
            </a>

            <div id='div_开放平台-公司详情-公司标签test_tag' class="popup_window">
                <div style='text-align: right; color:red; cursor:pointer;'>
                <a onfocus='this.blur();' onclick="document.getElementById('div_开放平台-公司详情-公司标签test_tag').style.display = 'none' " >
                   [x]</a>
                </div>
                <pre>
公司详情标签列表接口,返回的标签列表不全,返回的标签列表个数预期为69个,现在个数及标签列表为: 1  叉车销售 http://172.30.237.227:2013/corp/detail/tags?=&corpId=3979329963911125625
-------------------- >> begin captured logging << --------------------
urllib3.connectionpool: DEBUG: Starting new HTTP connection (1): 172.30.237.227:2013
urllib3.connectionpool: DEBUG: http://172.30.237.227:2013 "GET /corp/detail/tags?=&corpId=3979329963911125625 HTTP/1.1" 200 None
--------------------- >> end captured logging << ---------------------
Traceback (most recent call last):
  File "/usr/lib64/python2.7/unittest/case.py", line 369, in run
    testMethod()
  File "/home/xinjie.wang/apiscript/api_core/test_corpDetailTag.py", line 58, in test_tag
    self.assertGreaterEqual(len(compTag),50,u'å¬å¸è¯¦ææ ç­¾åè¡¨æ¥å£,è¿åçæ ç­¾åè¡¨ä¸å¨,è¿åçæ ç­¾åè¡¨ä¸ªæ°é¢æä¸º69ä¸ª,ç°å¨ä¸ªæ°åæ ç­¾åè¡¨ä¸º: '+str(len(compTag))+"  "+str(','.join(compTag))+" "+recontent.url)
  File "/usr/lib64/python2.7/unittest/case.py", line 988, in assertGreaterEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/usr/lib64/python2.7/unittest/case.py", line 450, in fail
    raise self.failureException(msg)
AssertionError: å¬å¸è¯¦ææ ç­¾åè¡¨æ¥å£,è¿åçæ ç­¾åè¡¨ä¸å¨,è¿åçæ ç­¾åè¡¨ä¸ªæ°é¢æä¸º69ä¸ª,ç°å¨ä¸ªæ°åæ ç­¾åè¡¨ä¸º: 1  åè½¦éå® http://172.30.237.227:2013/corp/detail/tags?=&corpId=3979329963911125625
-------------------- >> begin captured logging << --------------------
urllib3.connectionpool: DEBUG: Starting new HTTP connection (1): 172.30.237.227:2013
urllib3.connectionpool: DEBUG: http://172.30.237.227:2013 "GET /corp/detail/tags?=&corpId=3979329963911125625 HTTP/1.1" 200 None
--------------------- >> end captured logging << ---------------------

                </pre>
            </div>
            <!--css div popup end-->

            </td>
        </tr></table>
    <table class='result_table'>
        <colgroup>
            <col align='left' width="50%"/>
            <col align='right' width="10%" id="results_count"/>
            <col align='right' width="10%" id="results_passed"/>
            <col align='right' width="10%" id="results_failed"/>
            <col align='right' width="10%" id="results_errors"/>
            <col align='right' width="10%"/>
        </colgroup>
        <!-- test list end -->
        <tr id='total_row'>
            <td>Total</td>
            <td>25</td>
            <td>24</td>
            <td>1</td>
            <td>0</td>
            <td>&nbsp;</td>
        </tr>
    </table>
    <br/>
    <a href="javascript:void(0)" onclick="showRawLog(document.getElementById('rawoutput'))">Full log raw output</a>
    <div id='rawoutput' class='popup_window'>
        <pre>å¬å¸è¯¦ææ ç­¾åè¡¨æ¥å£,è¿åçæ ç­¾åè¡¨ä¸å¨,è¿åçæ ç­¾åè¡¨ä¸ªæ°é¢æä¸º69ä¸ª,ç°å¨ä¸ªæ°åæ ç­¾åè¡¨ä¸º: 1  åè½¦éå® http://172.30.237.227:2013/corp/detail/tags?=&corpId=3979329963911125625
-------------------- >> begin captured logging << --------------------
urllib3.connectionpool: DEBUG: Starting new HTTP connection (1): 172.30.237.227:2013
urllib3.connectionpool: DEBUG: http://172.30.237.227:2013 "GET /corp/detail/tags?=&corpId=3979329963911125625 HTTP/1.1" 200 None
--------------------- >> end captured logging << ---------------------Traceback (most recent call last):
  File "/usr/lib64/python2.7/unittest/case.py", line 369, in run
    testMethod()
  File "/home/xinjie.wang/apiscript/api_core/test_corpDetailTag.py", line 58, in test_tag
    self.assertGreaterEqual(len(compTag),50,u'å¬å¸è¯¦ææ ç­¾åè¡¨æ¥å£,è¿åçæ ç­¾åè¡¨ä¸å¨,è¿åçæ ç­¾åè¡¨ä¸ªæ°é¢æä¸º69ä¸ª,ç°å¨ä¸ªæ°åæ ç­¾åè¡¨ä¸º: '+str(len(compTag))+"  "+str(','.join(compTag))+" "+recontent.url)
  File "/usr/lib64/python2.7/unittest/case.py", line 988, in assertGreaterEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/usr/lib64/python2.7/unittest/case.py", line 450, in fail
    raise self.failureException(msg)
AssertionError: å¬å¸è¯¦ææ ç­¾åè¡¨æ¥å£,è¿åçæ ç­¾åè¡¨ä¸å¨,è¿åçæ ç­¾åè¡¨ä¸ªæ°é¢æä¸º69ä¸ª,ç°å¨ä¸ªæ°åæ ç­¾åè¡¨ä¸º: 1  åè½¦éå® http://172.30.237.227:2013/corp/detail/tags?=&corpId=3979329963911125625
-------------------- >> begin captured logging << --------------------
urllib3.connectionpool: DEBUG: Starting new HTTP connection (1): 172.30.237.227:2013
urllib3.connectionpool: DEBUG: http://172.30.237.227:2013 "GET /corp/detail/tags?=&corpId=3979329963911125625 HTTP/1.1" 200 None
--------------------- >> end captured logging << ---------------------
2
32766269
{"keywords": "\u91d1\u878d", "type": "1", "andOr": "1"}
</pre>
    </div>
</body>
</html>
"""

message = MIMEText(mail_message,'html','utf-8') #发送含有html内容的邮件

message['To'] = ",".join(receivers)
message['From'] = sender


#邮件标题

subject = '这是一封测试邮件' + str_time         #标题加上发送时间

message['Subject'] = Header(subject,'utf-8')    #设置编码

try:
    smtpobj = smtplib.SMTP_SSL('smtp.163.com',465)  #网易163邮箱 使用非本地服务器，需要建立和网易邮件服务 的SSL链接，端口465
    smtpobj.login(sender,pwd)
    smtpobj.sendmail(sender,receivers,message.as_string())  #发送邮件主题
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败,失败原因:',e)