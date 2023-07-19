let logged = true;

function getSelectValues(select) {
  var result = [];
  var options = select && select.options;
  var opt;
  for (var i = 0, iLen = options.length; i < iLen; i++) {
    opt = options[i];

    if (opt.selected) {
      result.push(opt.value || opt.text);
    }
  }

  return result;
}

function Register() {
  location.href = "../templates/register.html";
}
function submitRegister() {
  var el = document.getElementsByTagName("select")[0];
  console.log(getSelectValues(el));
}
function close_blog_popup() {
  //set opacity to zero
  $(document).ready(function () {
    $("#blog_popup").css("opacity", "0");
  });
}
function open_blog_popup() {
  //set opacity to zerol
  let logged = true;
  if (logged) {
    $("#blog_popup").css("opacity", "1");
  }
}
