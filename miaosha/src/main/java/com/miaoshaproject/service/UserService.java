package com.miaoshaproject.service;

import com.miaoshaproject.service.model.UserModel;

/**
 * Create by lxd on 2018/12/24.
 */
public interface UserService {
    //通过用户ID获取用户对象的方法
    UserModel getUserById(Integer id);
}
