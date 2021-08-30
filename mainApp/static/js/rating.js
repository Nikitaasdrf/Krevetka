const ratings = document.querySelectorAll('.rating');

if (ratings.length > 0) {
   initRatings();
}

//Основная функция
function initRatings() {
   let ratingActive, ratingValue;
   //Бегаем по всем рейтингам на странице
   for (let index = 0; index < ratings.length; index++) {
      const rating = ratings[index];
      initRating(rating);
   }

   //Инициализируем конкретный рейтинг
   function initRating(rating) {
      initRatingVars(rating);

      setRatingActiveWidth();


      if (rating.classList.contains('rating_set')) {
         setRating(rating);
      }
   }

   //Инициализация переменных
   function initRatingVars(rating) {
      ratingActive = rating.querySelector('.rating_active');
      ratingValue = rating.querySelector('.rating_value');
   }

   //Изменяем ширину активных звезд
   function setRatingActiveWidth(index = ratingValue.innerHTML) {
      const ratingActiveWidth = index / 0.05;
      ratingActive.style.width = `${ratingActiveWidth}%`;
   }

   //Возможность указать оценку
   function setRating(rating) {
      const ratingItems = rating.querySelectorAll('.rating_item');
      for (let index = 0; index < ratingItems.length; index++) {
         const ratingItem = ratingItems[index];
         ratingItem.addEventListener("mouseenter", function (e) {
            //Обновление переменных
            initRatingVars(rating);
            //Обновление активных звезд
            setRatingActiveWidth(ratingItem.value);
         });
         ratingItem.addEventListener("mouseleave", function (e) {
            //Обновление активных звезд
            setRatingActiveWidth();
         });
         ratingItem.addEventListener("click", function (e) {
            //Обновление переменных
            initRatingVars(rating);
            if (rating.dataset.ajax) {
               //"Отправить" на сервер
               setRatingValue(ratingItem.value, rating);
            } else {
               //Отобразить указанную оценку
               ratingValue.innerHTML = index + 1;
               setRatingActiveWidth();
            }
         });
      }
   }
}

// ###################Слайдер###############################
$(document).ready(function(){
   $('.slider').slick({
      arrows:true,
      dots:true,
   });
});
// ###################Бургер###############################
$(document).ready(function(){
   $('.header_burger').click(function(event) {
      $('.header_burger,.navigation-site').toggleClass('active');
      $('body').toggleClass('lock');
   });
});
// ########################### Перемещение элемента на новую строчку ##########################################
"use strict";

function DynamicAdapt(type) {
	this.type = type;
}

DynamicAdapt.prototype.init = function () {
	const _this = this;
	// массив объектов
	this.оbjects = [];
	this.daClassname = "_dynamic_adapt_";
	// массив DOM-элементов
	this.nodes = document.querySelectorAll("[data-da]");

	// наполнение оbjects объктами
	for (let i = 0; i < this.nodes.length; i++) {
		const node = this.nodes[i];
		const data = node.dataset.da.trim();
		const dataArray = data.split(",");
		const оbject = {};
		оbject.element = node;
		оbject.parent = node.parentNode;
		оbject.destination = document.querySelector(dataArray[0].trim());
		оbject.breakpoint = dataArray[1] ? dataArray[1].trim() : "767";
		оbject.place = dataArray[2] ? dataArray[2].trim() : "last";
		оbject.index = this.indexInParent(оbject.parent, оbject.element);
		this.оbjects.push(оbject);
	}

	this.arraySort(this.оbjects);

	// массив уникальных медиа-запросов
	this.mediaQueries = Array.prototype.map.call(this.оbjects, function (item) {
		return '(' + this.type + "-width: " + item.breakpoint + "px)," + item.breakpoint;
	}, this);
	this.mediaQueries = Array.prototype.filter.call(this.mediaQueries, function (item, index, self) {
		return Array.prototype.indexOf.call(self, item) === index;
	});

	// навешивание слушателя на медиа-запрос
	// и вызов обработчика при первом запуске
	for (let i = 0; i < this.mediaQueries.length; i++) {
		const media = this.mediaQueries[i];
		const mediaSplit = String.prototype.split.call(media, ',');
		const matchMedia = window.matchMedia(mediaSplit[0]);
		const mediaBreakpoint = mediaSplit[1];

		// массив объектов с подходящим брейкпоинтом
		const оbjectsFilter = Array.prototype.filter.call(this.оbjects, function (item) {
			return item.breakpoint === mediaBreakpoint;
		});
		matchMedia.addListener(function () {
			_this.mediaHandler(matchMedia, оbjectsFilter);
		});
		this.mediaHandler(matchMedia, оbjectsFilter);
	}
};

DynamicAdapt.prototype.mediaHandler = function (matchMedia, оbjects) {
	if (matchMedia.matches) {
		for (let i = 0; i < оbjects.length; i++) {
			const оbject = оbjects[i];
			оbject.index = this.indexInParent(оbject.parent, оbject.element);
			this.moveTo(оbject.place, оbject.element, оbject.destination);
		}
	} else {
		for (let i = 0; i < оbjects.length; i++) {
			const оbject = оbjects[i];
			if (оbject.element.classList.contains(this.daClassname)) {
				this.moveBack(оbject.parent, оbject.element, оbject.index);
			}
		}
	}
};

// Функция перемещения
DynamicAdapt.prototype.moveTo = function (place, element, destination) {
	element.classList.add(this.daClassname);
	if (place === 'last' || place >= destination.children.length) {
		destination.insertAdjacentElement('beforeend', element);
		return;
	}
	if (place === 'first') {
		destination.insertAdjacentElement('afterbegin', element);
		return;
	}
	destination.children[place].insertAdjacentElement('beforebegin', element);
}

// Функция возврата
DynamicAdapt.prototype.moveBack = function (parent, element, index) {
	element.classList.remove(this.daClassname);
	if (parent.children[index] !== undefined) {
		parent.children[index].insertAdjacentElement('beforebegin', element);
	} else {
		parent.insertAdjacentElement('beforeend', element);
	}
}

// Функция получения индекса внутри родителя
DynamicAdapt.prototype.indexInParent = function (parent, element) {
	const array = Array.prototype.slice.call(parent.children);
	return Array.prototype.indexOf.call(array, element);
};

// Функция сортировки массива по breakpoint и place 
// по возрастанию для this.type = min
// по убыванию для this.type = max
DynamicAdapt.prototype.arraySort = function (arr) {
	if (this.type === "min") {
		Array.prototype.sort.call(arr, function (a, b) {
			if (a.breakpoint === b.breakpoint) {
				if (a.place === b.place) {
					return 0;
				}

				if (a.place === "first" || b.place === "last") {
					return -1;
				}

				if (a.place === "last" || b.place === "first") {
					return 1;
				}

				return a.place - b.place;
			}

			return a.breakpoint - b.breakpoint;
		});
	} else {
		Array.prototype.sort.call(arr, function (a, b) {
			if (a.breakpoint === b.breakpoint) {
				if (a.place === b.place) {
					return 0;
				}

				if (a.place === "first" || b.place === "last") {
					return 1;
				}

				if (a.place === "last" || b.place === "first") {
					return -1;
				}

				return b.place - a.place;
			}

			return b.breakpoint - a.breakpoint;
		});
		return;
	}
};

const da = new DynamicAdapt("max");
da.init();

// ########################### Полет товара в карзину ##########################################
$('.addtocart').on('click', function(){
	var that = $(this).closest('.unit').find('img');
   var bascket = $(".style-img-basket");
   var w = that.width();

	that.clone()
	.css({'width' : w,
	'position' : 'absolute',
	'z-index' : '9999',
	top: that.offset().top,
	left:that.offset().left})
	.appendTo("body")
	.animate({opacity: 0.05,
		left: bascket.offset()['left'],
		top: bascket.offset()['top'],
		width: 20}, 300, function() {
			$(this).remove();
		});
});


$(document).ready(function(){
   $('.nik2').click(function(event) {
      $('.nik2').toggleClass('is-flipped');
   });
});
// ################ Переход в makingorder ##################
$("#gotoorder").click(function (){
	totlPrice = $("#TotlPriceID").text();
	if(totlPrice == "0"){alert("Вы ничего не заказали")}else{location.href = "/makingorder"};
});
// ######################### Информация о заказе ################################
$(".stylebtnmak").click(function(){
	$("#stylebtnmak").hide();
	$(".form-makingorder-beforeload").hide();
	$(".preloader-order").fadeIn();
	$(".preloader-order").delay(3700).fadeOut();
	$(".form-makingorder-afterload").delay(4500).fadeIn();
});
// ############################ Настройка чекбокса ################################
$(document).ready(function() {
	valRadio = $(".blockse").text()
	if(valRadio == ""){$(this).hide();}
});