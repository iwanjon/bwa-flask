
from flask import request
from flask_jwt_extended import jwt_required, get_jwt
from flask_restful import Resource
from marshmallow import ValidationError
from helper.error import NewError
from helper.responseFormatter import response_formatter
from models.campaign import CampignModel
from schemas.campaign import CampaignSchema
from services.campaign import Campaignservice
from services.user import UserService
# func (h *campaignHandler) UpdateCampaign(c *gin.Context) {
# 	var input campaign.GetCampaignDetailInput

# 	err := c.ShouldBindUri(&input)
# 	if err != nil {

# 		responseuser := helper.APIResponse("error updated campaign", http.StatusBadRequest, "error", err.Error())
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}

# 	var inputdata campaign.CreateCampaignInput

# 	err = c.ShouldBindJSON(&inputdata)

# 	if err != nil {
# 		errors := helper.FormatValidationError(err)
# 		errormessage := gin.H{"errors": errors}
# 		responseuser := helper.APIResponse("error update campaign", http.StatusBadRequest, "error", errormessage)
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}
# 	userid := c.MustGet("curresntuser").(user.User)
# 	inputdata.User = userid

# 	updated, err := h.service.UpdateCampaign(input, inputdata)
# 	if err != nil {
# 		responseuser := helper.APIResponse("error update campaign", http.StatusBadRequest, "error", nil)
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}
# 	responseuser := helper.APIResponse("success Update campaign", http.StatusOK, "success", campaign.FormatCampaign(updated))
# 	c.JSON(http.StatusOK, responseuser)

# }

# func (h *campaignHandler) CreateCampaign(c *gin.Context) {
# 	var input campaign.CreateCampaignInput

# 	err := c.ShouldBindJSON(&input)

# 	if err != nil {
# 		errors := helper.FormatValidationError(err)
# 		errormessage := gin.H{"errors": errors}
# 		responseuser := helper.APIResponse("error create campaign", http.StatusBadRequest, "error create campaign", errormessage)
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}
# 	userid := c.MustGet("curresntuser").(user.User)
# 	input.User = userid

# 	newcampaign, err := h.service.CreateCampaign(input)
# 	if err != nil {
# 		responseuser := helper.APIResponse("error create campaign", http.StatusBadRequest, "error create campaign", nil)
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}
# 	responseuser := helper.APIResponse("success create campaign", http.StatusOK, "success create campaign", campaign.FormatCampaign(newcampaign))
# 	c.JSON(http.StatusOK, responseuser)

# }

# func (h *campaignHandler) GetCampaigns(c *gin.Context) {
# 	userId, _ := strconv.Atoi(c.Query("user_id"))

# 	campaigs, err := h.service.FindCampaigns(userId)
# 	if err != nil {
# 		errors := helper.FormatValidationError(err)
# 		errormessage := gin.H{"errors": errors}
# 		responseuser := helper.APIResponse("error requet", http.StatusBadRequest, "error", errormessage)
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}

# 	responseuser := helper.APIResponse("success", http.StatusOK, "success", campaign.FormatCampaigns(campaigs))
# 	c.JSON(http.StatusOK, responseuser)

# }

# func (h *campaignHandler) GetCampaign(c *gin.Context) {
# 	var input campaign.GetCampaignDetailInput

# 	err := c.ShouldBindUri(&input)
# 	if err != nil {

# 		responseuser := helper.APIResponse("error INPUT", http.StatusBadRequest, "error", err.Error())
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}

# 	campain, err := h.service.GetCampaignById(input)
# 	if err != nil {

# 		responseuser := helper.APIResponse("error fet detail", http.StatusBadRequest, "error", err.Error())
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}
# 	responseuser := helper.APIResponse("success", http.StatusOK, "success", campaign.FormatCampaignDetail(campain))
# 	c.JSON(http.StatusOK, responseuser)

# }

# func (h *campaignHandler) UploadCampaignImage(c *gin.Context) {
# 	var input campaign.CreateCampaignImageInput

# 	err := c.ShouldBind(&input)
# 	if err != nil {
# 		errors := helper.FormatValidationError(err)
# 		errormessage := gin.H{"errors": errors}
# 		responseuser := helper.APIResponse("error upload campaign images", http.StatusBadRequest, "error", errormessage)
# 		c.JSON(http.StatusBadRequest, responseuser)
# 		return
# 	}
# 	file, err := c.FormFile("file")
# 	if err != nil {
# 		data := gin.H{"is_upload": false}
# 		response := helper.APIResponse("failed to upload campaign images", http.StatusBadRequest, "error", data)
# 		c.JSON(http.StatusBadRequest, response)
# 		return
# 	}
# 	currentUser := c.MustGet("curresntuser").(user.User)
# 	input.User = currentUser
# 	userId := currentUser.ID

# 	path := fmt.Sprintf("images/campaign-%d-%s", userId, file.Filename)

# 	err = c.SaveUploadedFile(file, path)
# 	if err != nil {
# 		data := gin.H{"is_upload": false}
# 		response := helper.APIResponse("failed to upload campaign images", http.StatusBadRequest, "error", data)
# 		c.JSON(http.StatusBadRequest, response)
# 		return
# 	}

# 	_, err = h.service.SaveCampaignImage(input, path)
# 	if err != nil {
# 		data := gin.H{"is_upload": false}
# 		response := helper.APIResponse(err.Error(), http.StatusBadRequest, "error", data)
# 		c.JSON(http.StatusBadRequest, response)
# 		return
# 	}

# 	data := gin.H{"is_upload": true}
# 	response := helper.APIResponse("success to upload campaign images", http.StatusOK, "success", data)
# 	c.JSON(http.StatusOK, response)
# }

campaignSchema = CampaignSchema()

# class UpdateCampaign:
#     @classmethod
#     def post(cls):
#         try:
#             campaignModel = campaignSchema.load(request.get_json())
#         except ValidationError as err:
#             return err.messages, 400
#         campaign_updated=Campaignservice.update_campaign(campaignModel)
#         return response_formatter("update sukses", 201,"sukses",campaignSchema.dump(campaign_updated) ), 201
        
class CreateCampaign(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        # print(get_jwt().get("sub"), get_jwt().get("lop"), "alll of that")
        user_id = get_jwt().get("sub")
        if not user_id:
            return "user not found", 400
        existing = UserService.get_user_by_id(user_id)
        if not existing:
            return "user not found", 400
        try:
            campaignModel:CampignModel = campaignSchema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        campaignModel.user_id = user_id
        print(campaignModel.name)
        campaign_cerated = Campaignservice.create_campaign(campaignModel)
        return response_formatter("update sukses", 201,"sukses",campaignSchema.dump(campaign_cerated) ), 201
        
class SingleCampaign(Resource):
    @classmethod
    @jwt_required()
    def get(cls, campaign_id):
        campign_first = Campaignservice.get_campaign_by_id(campaign_id)
        return response_formatter("update sukses", 201,"sukses",campaignSchema.dump(campign_first) ), 201
    @classmethod
    def put(cls, campaign_id):
        try:
            campaignModel = campaignSchema.load(request.get_json())
            campaignModel.id = campaign_id
        except ValidationError as err:
            return err.messages, 400
        try:
            campaign_updated=Campaignservice.update_campaign(campaignModel)
        except NewError as e:
            return e.NewMessage, 400
        return response_formatter("update sukses", 201,"sukses",campaignSchema.dump(campaign_updated) ), 201
                

class GetCampigns:
    pass

class SaveCampaignImage:
    pass