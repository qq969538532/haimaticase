class LoginConfig:
    dev_host = 'https://api.pre.hzmantu.com'  # 测试地址
    h5_host = 'https://api.pre.hzmantu.com'  # h5测试地址
    bms_host = 'https://api.pre.hzmantu.com'  # bms测试地址
    store_host = 'https://api.pre.hzmantu.com'# 门店测试地址
    release_host = 'project-cloud.dev.hzmantu.com'  # release环境
    bms_headers = {'x-stream-id': '.5PXiU8jDFbS0qj4cRSPVlYmbciD9L86'}
    store_headers = {'x-stream-id': '.2eRl2HaIQLbfpBFab0Qw6mxF6avBJDO'}
    cloud_jdbc_pool = 'cloud_test'  # 数据库缓冲池配置
    cloud_database_schemas = 'project-cloud'  # 云端数据库
    himo_store_host = 'api.pre.hzmantu.com'  # 海马体门店测试地址
    himo_store_jdbc_pool = 'cloud_test'  # 数据库缓冲池配置
    out_photographer_host = 'api.dev.hzmantu.com'  # 外包摄影测试地址
    cloud_user_id = 613646  # 云端登录staff_user_id
    cloud_login_url = 'https://sso.pre.hzmantu.com'  # sso登录地址
    cloud_login_path = '100'  # 云端快速登录参数
    himo_store_user_id = 613646  # 门店登录staff_user_id
    himo_store_login_url = 'sso.pre.hzmantu.com'  # sso登录地址
    himo_store_login_path = 1121  # 海马体快速登录参数
    xps_photo_1 = '2020/05/05/lkJ-RF6L_q3ropNBQANaAofLbJDm.jpg'  # 修片师上传的文件名
    xps_photo_2 = '2020/05/05/ls_Exc5QZiRvpWVbgjJT6Bq4wQk_.jpg'
    xps_photo_3 = '2020/05/05/lnsxgvJZ1GInQn7cgGd-sGSDFOWz.jpg'
    xps_photo_4 = '2020/05/05/liq9QTWtkNpbPrFS9FyZISGEJM9O.jpg'
    xps_jhz = '2020/05/29/lnU4M4-w4Zox5hqV3yUiHViP2rlO.jpg'  # 结婚登记照
    sys_photo_1 = '2020/05/05/lkWd_6m82023L3kcvVyDxIGoPN0V.jpg'  # 摄影师上传照片
    sys_photo2_1 = '2020/05/05/lvnK1vUdPTcGPylaGyAMbk5lgUJd.jpg'  # 摄影师上传的文件名
    xps_photo2_1 = '2020/05/05/lqBK9h-NRZQYDdEeGqnvrLH78TkV.jpg'  # 修片师上传的文件名
    blue_no_modle = 368  # 蓝标无模板
    blue_modle = 369  # 蓝标模板照
    master_modle = 366  # 大师模板
    master_no_modle = 367  # 大师无模板
    mainto_modle = 365  # 缦图模板
    mainto_no_modle = 364  # 缦图无模板
    kids_no_modle = 363  # kids无模板
    retouch_class_product = 3374  # 修图标准测试产品
    cloud_staff_id = '613646'  # 云端配置员工id
    xps_staff_id = '613646'  # 测试修片师员工号,必须为登录cookies的用户id
    reviewer_staff_id = '613646'  # 测试审核员工号,必须为登录cookies的用户id
    sys_org_secret = '$argon2i$v=19$m=1024,t=2,p=2$R0dUU0RONDBFcGQ4S3UxWQ$z163apzLID407f//PNYj47TGDAu+iuSloMtUcq4VX4s'  # 测试摄影机构登录密码
    sys_org_account = 'tunyue'  # 测试摄影机构登录账号
    http_cloud = dev_host + 'project-cloud.dev.hzmantu.com'
    himo_test_store = 1095  # 测试下单的门店
    himo_store_product_id_birth = 8524  # 生日照单人
    himo_store_product_id_wenyi = 5592  # 文艺照单人-彩色
    himo_store_product_id_family = 5581  # 全家福
    himo_store_product_id_job = 5546  # 职业形象照abd
    himo_store_product_id_marriage = 5443  # 结婚登记照
    himo_store_product_id_visa = 5403  # 精致证件照
    himo_store_product_id_visa2 = 5499  # 精致证件照-正面(在线看片产品)
    himo_user_id = 4657991  # 海马体登录用户的user_id
    himo_store_uesr_id = 613646  # 海马体登录帐号id
    himo_art_photo_cloud_id = 15  # 文艺照云端id
    himo_store_kefu_staff_id = 606144  # 海马体门店客服id,用于摄影签到
    staff_cookies_0 = 'RbdkzgHt9Qf1QkDyk9ERDhLSVkEGvn0n'
    staff_cookies_1 = 'fqWoFnz1xvVyrUC1ahnwc3kTjhz2GY5D'
    staff_cookies_2 = 'Ogz6BRVxeP1ueh6M6XeZSg5axFmXbYrH'
    staff_cookies_3 = '63lmot5xi2WBoX2usokntlqHfbQw0wxb'
    staff_cookies_4 = 'Lf6fvSmmu918vs84fcilW1PeIIk69YTs'
    test_staff_id_0 = 613646
