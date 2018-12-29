package com.miaoshaproject.controller;

import com.miaoshaproject.error.BusinessException;
import com.miaoshaproject.error.EmBusinessError;
import com.miaoshaproject.response.CommonReturnType;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.Map;

/**
 * Create by lxd on 2018/12/27
 */

public class BaseController {

    public static final String CONTENT_TYPE_FORMED="application/x-www-from-urlencoded";

    //定义exceptionhandler解决未被controller层吸收的exception
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.OK)
    @ResponseBody
    public Object handlerException(HttpServletRequest request, Exception ex){
//        CommonReturnType commonReturnType = new CommonReturnType();
        Map<String,Object> responeData = new HashMap<>();
        if (ex instanceof BusinessException){
            BusinessException businessException = (BusinessException)ex;
            responeData.put("essCode",businessException.getErrCode());
            responeData.put("essMsg",businessException.getErrMsg());
        }else{
            responeData.put("essCode", EmBusinessError.UNKNOWN_ERROR.getErrCode());
            responeData.put("essMsg",EmBusinessError.UNKNOWN_ERROR.getErrMsg());
        }
        return CommonReturnType.create(responeData,"fail");
    }
}
