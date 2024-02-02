def response_formatter(message = None, code= 400, status= "error", data=None):
    meta = dict(
        message = message,
        code = code,
        status= status,
    )
    response = dict(
        meta = meta,
        data= data
    )
    return response


def response_formatter_all(message = None, code= 400, status= "error", data=None, user_schema= None):
    meta = dict(
        message = message,
        code = code,
        status= status,
    )
    if data == []:
        response = dict(
            meta = meta,
            data= data
        )   
        return response 
    
    data_conv = []
    
    for i in data:
        data_conv.append(user_schema.dump(i))
    response = dict(
            meta = meta,
            data= data_conv
        )   
    return response 
	# meta := meta{
	# 	Message: message,
	# 	Code:    code,
	# 	Status:  status,
	# }
	# jsonresponse := response{
	# 	Meta: meta,
	# 	Data: data,
	# }