/*日内交易数据分析，统计交易区间成交关系*/
"use strict"

const fs = require("fs");
const util = require('util');
const moment = require("moment")
const RootDir = "E:\\stockScan\\data";
let startDate = "2017-02-18"

let code = "002690";//002690
let dailyDateRoot = RootDir+"\\dailyTrade"
let date = moment().format("YYYY-MM-DD");
let filepath = dailyDateRoot+"\\"+code+"\\"+startDate+".json";

var getDailyData = function(path,time){
	let jsonData;
	try{
		jsonData = fs.readFileSync(path, {"encoding":"utf-8"});
		if(jsonData.length<300){
			return;
		}
		jsonData = JSON.parse(jsonData);
		let buyer=0,seller=0,buycount=0,sellcount=0,buy=0,sell=0,midder=0,mid=0,midcount=0;
		for(let i in jsonData){
			//console.warn(jsonData['amount'])
			if(jsonData[i].type=="买盘"){
				++buyer;
				buycount = buycount + jsonData[i]['volume']*1;
				buy = buy+jsonData[i]['amount']*1;
			}else if(jsonData[i].type=="卖盘"){
				++seller;
				sellcount = sellcount + jsonData[i]['volume']*1;
				sell = sell+jsonData[i]['amount']*1;
			}else{
				++midder;
				midcount = midcount + jsonData[i]['volume']*1;
				mid = mid+jsonData[i]['amount']*1;
			}
		}
		console.log(time +"交易数据");
		console.log("净流入"+(buy-sell)/10000+"万元");
		console.log(buyer+"手买盘"+buycount +"占比"+buy/(buy+sell+mid).toFixed(3));
		console.log(seller+"手卖盘"+sellcount +"占比"+sell/(buy+sell+mid).toFixed(3));
		console.log(midder+"手中性盘"+midcount +"成交"+mid/10000+"万元" +"占比"+mid/(buy+sell+mid).toFixed(3));
		console.log("\n");
	}catch(e){
		return;
	}
}

let diffDay = parseInt((moment().format("X") - moment(startDate).format("X"))/86400)

for(let i=0;i<diffDay;i++){
	startDate = moment(startDate).add(1,"day").format("YYYY-MM-DD");
	filepath = dailyDateRoot+"\\"+code+"\\"+startDate+".json";
	getDailyData(filepath,startDate)
}
