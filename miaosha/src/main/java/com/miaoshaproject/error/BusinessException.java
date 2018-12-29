package com.miaoshaproject.error;

/**
 * Create by lxd on 2018/12/26
 */

//包装器业务异常类实现
public class BusinessException extends Exception implements CommonError {
   private CommonError commonError;
   //直接接收EmBusinessError的传参用于构造业务异常
   public BusinessException(CommonError commonError){
       super();
       this.commonError=commonError;
   }

   //接收自定义errMsg的方法构造业务异常
    public BusinessException(CommonError commonError,String errMsg){
       super();
       this.commonError = commonError;
       this.commonError.setErrMsg(errMsg);
    }

    @Override
    public int getErrCode() {

       return commonError.getErrCode();
    }

    @Override
    public String getErrMsg() {

       return commonError.getErrMsg();
    }

    @Override
    public CommonError setErrMsg(String errMsg) {
        this.commonError.setErrMsg(errMsg);
       return this;
    }
}
