var key = "64e226ee33ac6ebdfba50575943e071754650daf";

var url =  "https://api.getgeoapi.com/v2/currency/list?api_key=" + key + "&format=json"

$.getJSON(url, function (data) {
    console.log(data);
});