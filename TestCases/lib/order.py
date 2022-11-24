# -*- coding:utf-8 -*-
# 订单模块

def postOrderData():
    """ 添加登录用户body模板 """
    data = {
  "receiveId": 1640,
  "couponId": 0,
  "price": "1.00",
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
          "skuId": 2091,
          "number": 1,
          "selected": 1,
          "platformSeckillId": 0,
          "platformDiscountId": 0,
          "shopSeckillId": 0,
          "shopDiscountId": 0,
          "priceId": 0,
          "composeId": 0,
          "sceneId": 0,
          "buyerCouponId": 0,
          "buyerShopCouponId": 0
        }
      ]
    }
  ],
  "discountPrice": 0
}

    return data