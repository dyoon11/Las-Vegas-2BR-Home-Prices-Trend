# Las Vegas 2 Bed Room Home Price Trend

## Introduction
The purpose of this research is to see which neighborhoods in Las Vegas has the most affordable 2 bedroom housing and which neighborhoods have the most expensive homes over a 20+ year period. The research will consist of Zillow's home data and python will be used to manipulate the data and provide an answer to the question.

## Dataset
There are two datasets with a sample size of home prices across the United States that will be used. Both are from Zillow's webiste and will have 20+ years of home price data (averaged and aggregated by month). 
* Neighborhood 2 bedroom home price data
* City 2 bedroom home price data
https://www.zillow.com/research/data/

## Neighborhoods
There are over 30+ neighborhoods in Las Vegas:
* Paradise
* Spring Valley
* Sunrise Manor
* Enterprise
* Centennial Hills
* Lone Mountain
* Summerlin North
* Michael Way
* North Cheyenne
* Charleston Heights
* Summerlin South
* Whitney
* Rancho Charleston
* East Las Vegas
* The Lakes
* Winchester
* Sheep Mountain
* West Las Vegas
* Tule Springs
* Sunrise
* Buffalo
* Huntridge
* Pioneer Park
* Desert Shores
* Cultural Corridor
* Angel Park Lindell
* Downtown
* Twin Lakes
* Sun City Summerlin
* Downtown East
* University Medical Center
* The Strip
* Queensridge

## Analysis

As we can see from the time series plot, all the neighborhoods follow a similar pattern with an increase from 2000-2008 and then a decrease up to 2012 and then an increase to present time. 

### Top 5 Neighborhoods in Las Vegas 2 BR AVG 20 Yr Prices
1. The Strip - $484488
2. Queensridge - $449178
3. Summerlin South - $349058
4. Downtown - $254567
5. Sun City Summerlin - $247983

### Bottom 5 Neighborhoods in Las Vegas 2 BR AVG 20 Yr Prices 
1. Cultural Corridor - $101731
2. East Las Vegas - $103779
3. Buffalo - $108150
4. West Las Vegas - $111890
5. Sunrise - $113230

![image](https://github.com/dyoon11/Las-Vegas-2BR-Home-Prices-Trend/assets/147287123/3d56b1fa-2693-41a6-946b-7b8352204c95)

## Prediction/Limitation

As we are able to have historical prices of the neighborhoods in Las Vegas, we are able to predict the future prices for 2024. However, there are some limitations that go along with this. Since we have limited data, there is limited visibility in terms of future home prices. Home prices are constantly being affected by demand, supply, inflation, and interest rates. Since we only have past home data, what we are able to see will not truly affect what may happen. Nevertheless, we have trained a bot to take into consideration all the past home prices in Las Vegas and predict the next couple of months. 
