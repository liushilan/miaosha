package com.miaoshaproject.error;

public enum EmBusinessError implements CommonError{
    //通用错位类型10001
    PAPAMETER_VALIDATION_ERROR(10001,"参数不合法"),
    UNKNOWN_ERROR(10002,"未知错位"),

    //2000开头为用户信息相关错位定义
    USER_NOT_EXIST(20001,"用户信息不存在"),

    ;

    private EmBusinessError(int errCode,String errMsg){
        this.errCode=errCode;
        this.errMsg=errMsg;
    }
    private int errCode;
    private String errMsg;
    @Override
    public int getErrCode() {

        return this.errCode;
    }

    @Override
    public String getErrMsg() {

        return this.errMsg;
    }

    @Override
    public CommonError setErrMsg(String errMsg) {
        this.errMsg=errMsg;
        return this;
    }
}
