//import Cookies from "js-cookie";

var x, i, j, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  /* For each element, create a new DIV that will act as the selected item: */
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /* For each element, create a new DIV that will contain the option list: */
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < selElmnt.length; j++) {
    /* For each option in the original select element,
    create a new DIV that will act as an option item: */
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
        var y, i, k, s, h;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        h = this.parentNode.previousSibling;
        for (i = 0; i < s.length; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            for (k = 0; k < y.length; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }
        h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  for (i = 0; i < y.length; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < x.length; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var recordCard = function(number) {
    const csrftoken = getCookie('csrftoken');
    const form = document.querySelector('form');
    var relation = Date.now();
    var data = Object.fromEntries(new FormData(form).entries());
    var picture = document.querySelector('input[type="file"]');
    var formData = new FormData();
    console.log("[CARD FORM]", data);
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append('user_id', number);
    formData.append("card_first_name", data.card_first_name);
    formData.append("card_last_name", data.card_last_name);
    formData.append("card_phone_number", data.card_phone_number);
    formData.append("card_region", data.card_region);
    formData.append("card_text", data.card_desc);
    formData.append("relation", relation);
    var request = new Request(
    "add/card",
    {
        headers: {
        "X-Requested-With": "XMLHttpRequest",
        'X-CSRFToken': csrftoken,
        }
    }
    );

    fetch(request, {
        method: "POST",
        mode: "cors",
        cache: "default",
        credentials: 'include',
        body: formData,
    }).then(function(response) {
        console.log(response);
    });

    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append('user_id', number);
    formData.append('image', picture.files[0]);
    formData.append("relation", relation);
    request = new Request(
    "add/image",
    {
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            'X-CSRFToken': csrftoken
        }
    }
    );
    fetch(request, {
        method: "POST",
        mode: "cors",
        cache: "default",
        credentials: 'include',
        body: formData,
    }).then(function(response) {
        console.log("image", response);
    })
};

var sendSender = function(user_id, service_id, relation) {
    const csrftoken = getCookie('csrftoken');
    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append("user_id", user_id);
    formData.append("service_id", service_id);
    formData.append("relation", relation);
    console.log(formData, user_id, service_id, relation);
    var request = new Request(
    "send/service",
    {
        headers: {
        "X-Requested-With": "XMLHttpRequest",
        'X-CSRFToken': csrftoken,
        }
    }
    );

    fetch(request, {
        method: "POST",
        mode: "cors",
        cache: "default",
        credentials: 'include',
        body: formData,
    }).then(function(response) {
        console.log(response);
    });
//
//    var formData = new FormData();
//    formData.append('csrfmiddlewaretoken', csrftoken);
//    formData.append('user_id', number);
//    formData.append('image', picture.files[0]);
//    formData.append("relation", relation);
//    request = new Request(
//    "add/image",
//    {
//        headers: {
//            "X-Requested-With": "XMLHttpRequest",
//            'X-CSRFToken': csrftoken
//        }
//    }
//    );
//    fetch(request, {
//        method: "POST",
//        mode: "cors",
//        cache: "default",
//        credentials: 'include',
//        body: formData,
//    }).then(function(response) {
//        console.log("image", response);
//    })
};


/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);