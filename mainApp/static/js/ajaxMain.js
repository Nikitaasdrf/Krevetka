function getCookie(name) {
  var cookieArr = document.cookie.split(";");
  for(var i = 0; i < cookieArr.length; i++) {
      var cookiePair = cookieArr[i].split("=");
      if(name == cookiePair[0].trim()) {return decodeURIComponent(cookiePair[1]);}
  }
  return null;
}

var addProduct = JSON.parse(getCookie('addProduct'))

if (addProduct == undefined){
  addProduct = {}
  document.cookie ='addProduct=' + JSON.stringify(addProduct) + ";domain=;path=/"
}

function ajaxProducts() {
  productID = $(this).val()
  pictureurl = $('#' + productID + ' .img-unit' + ' img').attr('src')
  productname = $('#' + productID + ' .nameUnit').html()
  productcount = $('#' + productID + ' .btn-unit' + ' .form-control').val()
  productprice = $('#' + productID + ' .btn-unit' + ' .price').html()
  if (addProduct[productID] == undefined){addProduct[productID] = {'productcount':Number(productcount)}}
  else{addProduct[productID]['productcount'] += Number(productcount)}
  document.cookie ='addProduct=' + JSON.stringify(addProduct) + ";domain=;path=/"
  $.ajax ({
    url: '', 
    type: 'get',
    data: {
      pictureurl: pictureurl,
      productname: productname,
      productcount: productcount,
      productprice: productprice,
      productid: productID,
      check: 'additem',
    },
    success: function(response){
      $(".ItemCount").text(response.ItemCount)
    }
  }) 
}

function ajaxBasketOnload() {
  $.ajax ({
    url: '', 
    type: 'get',
    data: {
      check: 'pageonload',
    },
    success: function(response) {
      $(".ItemCount").text(response.ItemCount)
      $(".ItemWord").text(response.ItemWord)
      $(".TotlKg").text(response.TotlKg)
      $(".TotlPrice").text(response.TotlPrice)
      for (const el of response.AddProductsDictLst){
        $(".form-basket").append(
          '<div class="form-product"><img class="form-product2" src="'
          + el.PictureURL + 
          '" alt=""><span class="form-product3">' 
          + el.ProductName + 
          '</span><div class="form-product4"><input class="product-in" id="input' 
          + el.ProductID + 
          '" type="number" placeholder="1/КГ" min="1" value="' 
          + el.ProductCount + 
          '"></div><span class="form-product5" id="change'+ el.ProductID +'">' 
          + el.ProductPrice * el.ProductCount + 
          ' /кг</span><div class="form-product6"><button id="removebtn' + el.ProductID + '" class="btn btn-outline-danger">Удалить</button></div></div>'
          )
          $(".final-price-px-making2").prepend(
            '<div class="weight" ><span class="weight-text fontsize-1">'+ el.ProductName +
            '</span><span class="style-margin1 fontsize-1">'+ el.ProductCount + ' шт</span></div>'
          )
        }
      $(".form-product6 .btn").click(ajaxBasketRemoveItem)
    },
  }) 
}


function ajaxBasketRemoveItem() {
  itemid = $(this).attr('id').split('removebtn').join("");
  delete addProduct[itemid];
  document.cookie ='addProduct=' + JSON.stringify(addProduct) + ";domain=;path=/"
  $.ajax ({
    url: '', 
    type: 'get',
    data: {
      itemid: itemid,
      check: 'removeitem',
    },
    success: function(response) {
      $(".ItemCount").text(response.ItemCount)
      $(".ItemWord").text(response.ItemWord)
      $(".TotlKg").text(response.TotlKg)
      $(".TotlPrice").text(response.TotlPrice)
      $(".form-basket").empty()
      for (const el of response.AddProductsDictLst){
        $(".form-basket").append(
          '<div class="form-product"><img class="form-product2" src="'
          + el.PictureURL + 
          '" alt=""><span class="form-product3">' 
          + el.ProductName + 
          '</span><div class="form-product4"><input class="product-in" id="input' 
          + el.ProductID + 
          '" type="number" placeholder="1/КГ" min="1" value="' 
          + el.ProductCount + 
          '"></div><span class="form-product5" id="change'+ el.ProductID +'">'
          + el.ProductPrice * el.ProductCount +
          ' /кг</span><div class="form-product6"><button id="removebtn' + el.ProductID + '" class="btn btn-outline-danger">Удалить</button></div></div>'
          )
      }
      $(".form-product6 .btn").click(ajaxBasketRemoveItem)
    },
  }) 
}

function ajaxBasketChangeCount() {
  productID = $(this).attr('id').split('input').join("");
  productcountb = $('#input' + productID).val()
  addProduct[productID]['productcount'] = Number(productcountb)
  document.cookie ='addProduct=' + JSON.stringify(addProduct) + ";domain=;path=/"
  $.ajax ({
    url: '',
    type: 'get',
    data: {
      productcountb: productcountb,
      productidb: productID,
      check: 'changebasket'
    },
    success: function(response) {
      $(".TotlPrice").text(response.TotlPrice)
      $(".TotlKg").text(response.TotlKg)
      $("#change"+response.productidC).text(response.Dollarchange+"/кг")
    },
  })
}

function ajaxFinalOrder() {
  clientName = $('#clientName').val()
  clientsurName = $('#cliensurName').val()
  clientPhone = $('#clientPhone').val()
  clientEmail = $('#clientEmail').val()
  DeliveryMethod = $('#DeliveryMethod').val()
  clientAddress = $('#clientAddress').val()
  $.ajax ({
    url: '',
    type: 'get',
    data: {
      clientname: clientName,
      clientsurname: clientsurName,
      clientphone: clientPhone,
      clientemail: clientEmail,
      deliverymethod: DeliveryMethod,
      clientaddress: clientAddress,
      check: 'clientinfo',
    },
    success: function(response) {
      $(".nameCustomer").text(response.clientName)
      $(".numberOrderId").text(response.orderId)
    },
  })
}

function ajaxOnloadFinalOrder() {
  $.ajax ({
    url: '', 
    type: 'get',
    data: {
      check: 'pageonloadfinalorder',
    },
    success: function(response) {
      for (const el of response.ClientInfoNikita){
        $(".ordercolumn").append(
          '<div class="orderinprogressone '+ el.statusColor +'"><div class="whoclient co-st"><span class="infofield" id="nameClient">'+ el.NameClient +
          '</span> <span class="infofield" id="nameSurClient">'+ el.SurnameClient +
          '</span></div><div class="numemail co-st"><span class="infofield" id="clientPhone">'+ el.ClientPhone +
          '</span> <span class="infofield" id="clientEmail">'+ el.ClientEmail +
          '</span></div><div class="deliverymethod co-st"><span class="infofield" id="DeliveryMethod">'+ el.DeliveryMethod +
          '</span></div><div class="customeraddress co-st"><span class="infofield">'+ el.ClientAddress +'</span></div><div class="clientproducts co-st">'+ el.prname +
          '</div><div class="weightsumA co-st"><span class="infofield">'+ el.prcount +
          '</span> кг</div><div class="priceclient co-st"><span class="infofield">'+ el.prprice +
          '</span> ₽</div><div class="dataofcreation co-st"><span class="infofield">'+ el.dateOrder +
          '</span></div><div class="compleriondate co-st"><input type="date" id="dateinput'+ el.orderId +
          '"/><button class="getval" id="getinput'+ el.orderId +
          '">Отправить</button></br><span class="infofield" id="textdate'+ el.orderId +'">'+ el.dateDone +
          '</span></div><div class="managingstatus co-st"><select id="statusid'+ el.orderId +
          '" class="statusclass" type="text"><option class="option0" value="0" id="bc'+ el.orderId +'">'+ el.statusOrder +'</option><option value="На рассмотрении">На рассмотрении</option><option value="В работе">В работе</option><option value="В пути">В пути</option><option value="Выполнено">Выполнено</option></select><button id="delbtn'+ el.orderId +'" class="delord">Удалить</button></div></div>'
          )
      }
      for (const el of response.ClientInfoNikitaDone){
        $(".ordercolumnhistory").append(
          '<div class="orderinprogressone"><div class="whoclient co-st"><span class="infofield" id="nameClient">'+ el.NameClient +
          '</span> <span class="infofield" id="nameSurClient">'+ el.SurnameClient +
          '</span></div><div class="numemail co-st"><span class="infofield" id="clientPhone">'+ el.ClientPhone +
          '</span> <span class="infofield" id="clientEmail">'+ el.ClientEmail +
          '</span></div><div class="deliverymethod co-st"><span class="infofield" id="DeliveryMethod">'+ el.DeliveryMethod +
          '</span></div><div class="customeraddress co-st"><span class="infofield">'+ el.ClientAddress +'</span></div><div class="clientproducts co-st">'+ el.prname +
          '</div><div class="weightsumA co-st"><span class="infofield">'+ el.prcount +
          '</span> кг</div><div class="priceclient co-st"><span class="infofield">'+ el.prprice +
          '</span> ₽</div><div class="dataofcreation co-st"><span class="infofield">'+ el.dateOrder +
          '</span></div><div class="compleriondate co-st"><span class="infofield">'+ el.dateDone +
          '</span></div><div class="managingstatus co-st">'+ el.statusOrder +'</div></div>'
          )
      }
      $(".getval").click(ajaxDeliveryTime)
      $(".delord").click(ajaxRemoveFinalOrder)
    },
  }) 
}
function ajaxRemoveFinalOrder() {
  delbtnId = $(this).attr('id').split('delbtn').join("");
  $.ajax ({
    url: '',
    type: 'get',
    data: {
      delbtnid: delbtnId,
      check: 'removefinalorder',
    },
    success: function(response) {
      $(".ordercolumn").empty()
      for (const el of response.ClientInfoNikita){
        $(".ordercolumn").append(
          '<div class="orderinprogressone '+ el.statusColor +'"><div class="whoclient co-st"><span class="infofield" id="nameClient">'+ el.NameClient +
          '</span> <span class="infofield" id="nameSurClient">'+ el.SurnameClient +
          '</span></div><div class="numemail co-st"><span class="infofield" id="clientPhone">'+ el.ClientPhone +
          '</span> <span class="infofield" id="clientEmail">'+ el.ClientEmail +
          '</span></div><div class="deliverymethod co-st"><span class="infofield" id="DeliveryMethod">'+ el.DeliveryMethod +
          '</span></div><div class="customeraddress co-st"><span class="infofield">'+ el.ClientAddress +'</span></div><div class="clientproducts co-st">'+ el.prname +
          '</div><div class="weightsumA co-st"><span class="infofield">'+ el.prcount +
          '</span> кг</div><div class="priceclient co-st"><span class="infofield">'+ el.prprice +
          '</span> ₽</div><div class="dataofcreation co-st"><span class="infofield">'+ el.dateOrder +
          '</span></div><div class="compleriondate co-st"><input type="date" id="dateinput'+ el.orderId +
          '"/><button class="getval" id="getinput'+ el.orderId +
          '">Отправить</button></br><span class="infofield" id="textdate'+ el.orderId +'">'+ el.dateDone +
          '</span></div><div class="managingstatus co-st"><select id="statusid'+ el.orderId +
          '"type="text"><option class="option0" value="0">'+ el.statusOrder +'</option><option value="На рассмотрении">На рассмотрении</option><option value="В работе">В работе</option><option value="В пути">В пути</option><option class="DONE" value="Выполнена">Выполнена</option></select><button id="delbtn'+ el.orderId +'" class="delord">Удалить</button></div></div>'
          )
      }
      $(".getval").click(ajaxDeliveryTime)
      $(".delord").click(ajaxRemoveFinalOrder)
    },
  })
}
function ajaxDeliveryTime() {
  dateID = $(this).attr('id').split('getinput').join("");
  valDate = $('#dateinput' + dateID).val().split("-");
  textDate = valDate[2] + '.' + valDate[1] + '.' + valDate[0]
  $.ajax ({
    url: '',
    type: 'get',
    data: {
      dateid: dateID,
      valdate: textDate,
      check: 'newdate',
    },
    success: function(response) {
      $("#textdate" + dateID).text(response.valDate)
    },
  })
}
function ajaxNewStatus() {
  statusVal = $(this).val();
  if(statusVal == "В работе"){colorStatus = "colorsecond"}
  else if(statusVal == "В пути"){colorStatus = "colorthree"}
  else{colorStatus = "colorfirst"};
  statusId = $(this).attr('id').split('statusid').join("");
  $.ajax ({
    url: '',
    type: 'get',
    data: {
      statusval: statusVal,
      colorstatus: colorStatus,
      statusid: statusId,
      check: 'newstatus',
    },
    success: function(response) {
      $(".ordercolumn").empty()
      $(".ordercolumnhistory").empty()
      for (const el of response.ClientInfoNikita){
        $(".ordercolumn").append(
          '<div class="orderinprogressone '+ el.statusColor +'"><div class="whoclient co-st"><span class="infofield" id="nameClient">'+ el.NameClient +
          '</span> <span class="infofield" id="nameSurClient">'+ el.SurnameClient +
          '</span></div><div class="numemail co-st"><span class="infofield" id="clientPhone">'+ el.ClientPhone +
          '</span> <span class="infofield" id="clientEmail">'+ el.ClientEmail +
          '</span></div><div class="deliverymethod co-st"><span class="infofield" id="DeliveryMethod">'+ el.DeliveryMethod +
          '</span></div><div class="customeraddress co-st"><span class="infofield">'+ el.ClientAddress +'</span></div><div class="clientproducts co-st">'+ el.prname +
          '</div><div class="weightsumA co-st"><span class="infofield">'+ el.prcount +
          '</span> кг</div><div class="priceclient co-st"><span class="infofield">'+ el.prprice +
          '</span> ₽</div><div class="dataofcreation co-st"><span class="infofield">'+ el.dateOrder +
          '</span></div><div class="compleriondate co-st"><input type="date" id="dateinput'+ el.orderId +
          '"/><button class="getval" id="getinput'+ el.orderId +
          '">Отправить</button></br><span class="infofield" id="textdate'+ el.orderId +'">'+ el.dateDone +
          '</span></div><div class="managingstatus co-st"><select id="statusid'+ el.orderId +
          '" class="statusclass" type="text"><option class="option0" value="0">'+ el.statusOrder +'</option><option value="На рассмотрении">На рассмотрении</option><option value="В работе">В работе</option><option value="В пути">В пути</option><option value="Выполнено">Выполнено</option></select><button id="delbtn'+ el.orderId +'" class="delord">Удалить</button></div></div>'
          )
      }
      for (const el of response.ClientInfoNikitaDone){
        $(".ordercolumnhistory").append(
          '<div class="orderinprogressone"><div class="whoclient co-st"><span class="infofield" id="nameClient">'+ el.NameClient +
          '</span> <span class="infofield" id="nameSurClient">'+ el.SurnameClient +
          '</span></div><div class="numemail co-st"><span class="infofield" id="clientPhone">'+ el.ClientPhone +
          '</span> <span class="infofield" id="clientEmail">'+ el.ClientEmail +
          '</span></div><div class="deliverymethod co-st"><span class="infofield" id="DeliveryMethod">'+ el.DeliveryMethod +
          '</span></div><div class="customeraddress co-st"><span class="infofield">'+ el.ClientAddress +'</span></div><div class="clientproducts co-st">'+ el.prname +
          '</div><div class="weightsumA co-st"><span class="infofield">'+ el.prcount +
          '</span> кг</div><div class="priceclient co-st"><span class="infofield">'+ el.prprice +
          '</span> ₽</div><div class="dataofcreation co-st"><span class="infofield">'+ el.dateOrder +
          '</span></div><div class="compleriondate co-st"><span class="infofield">'+ el.dateDone +
          '</span></div><div class="managingstatus co-st">'+ el.statusOrder +'</div></div>'
          )
      }
    },
  })
}

///////Чат функции
function ajaxPageNikita() {
  inputNikita1 = $('#pagenikita1').val()
  $.ajax({
    url: '',
    type: 'get',
    data: {
      inputnikita1: inputNikita1,
      check: 'nikita'
    },
    success: function(response) {
      $("#nikitatest1").empty()
      for (const el of response.test){
        $("#nikitatest1").append(el.Input1)
      }
    },
  })
}
function ajaxPageOnLoadNikita() {
  $.ajax({
    url: '',
    type: 'get',
    data: {
      check: 'pageonloadnikita'
    },
    success: function(response) {
      for (const el of response.test){
        $("#nikitatest1").append(el.Input1)
      }
    },
  })
}

///////Чат функции
// $(document).ready(function (){
$('.btn-unit .btn').click(ajaxProducts)
$('#stylebtnmak').click(ajaxFinalOrder)
$('#pagenikita').click(ajaxPageNikita)
// })
$(document).on('change','.form-product4 .product-in', ajaxBasketChangeCount);
$(document).on('change','.managingstatus .statusclass', ajaxNewStatus);
$(window).on("load", ajaxOnloadFinalOrder);
$(window).on("load", ajaxBasketOnload);
$(window).on("load", ajaxPageOnLoadNikita);