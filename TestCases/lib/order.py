# -*- coding:utf-8 -*-
# 订单模块

def postOrderData():
    """ 添加订单body模板 """
    data = {
  "receiveId": 2027,
  "couponId": 0,
  "price": "99.00",
  "shops": [
    {
      "shopId": 95,
      "distribution": {
        "distributionPrice": 0,
        "logisticsId": 0,
        "distributionName": "全国包邮"
      },
      "skus": [
        {
          "skuId": 591,
          "number": 1,
          "selected": 1,
          "platformSeckillId": 0,
          "platformDiscountId": 0,
          "shopSeckillId": 0,
          "shopDiscountId": 0,
          "priceId": 0,
          "composeId": 0,
          "sceneId": 0,
          "useMember": 'false',
          "buyerCouponId": 0,
          "buyerShopCouponId": 0
        }
      ]
    }
  ],
  "discountPrice": 0
}

    return data