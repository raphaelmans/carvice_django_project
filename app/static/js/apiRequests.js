async function updateUserById() {
  const user_id = $("#modal_user_userid").val();
  const first_name = $("#modal_user_firstname").val();
  const last_name = $("#modal_user_lastname").val();
  const username = $("#modal_user_username").val();
  const password = $("#modal_user_password").val();

  const res = await fetch("http://127.0.0.1:8000/api/userById", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      user_id: user_id,
      username: username,
      first_name: first_name,
      last_name: last_name,
      password: password,
    }),
  });
  if (res.status == 200) {
    location.reload();
  }
}


async function openDeleteModal(user_id,model_type){  
    $("#deleteConfirmModal").modal('show')
    $("#delete_id").val(user_id)
    $("#delete_model_type").val(model_type)
}


async function deleteById() {
  const model_type = $("#delete_model_type").val();
  const id = $("#delete_id").val();
  let deleteLink = "http://127.0.0.1:8000/api";
  let reqBodyValue = null;
  switch (model_type) {
    case "USER":
      deleteLink = `${deleteLink}/userById`;
      reqBodyValue = JSON.stringify({
        user_id: id,
      });
      break;
  }
  const res = await fetch(deleteLink, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: reqBodyValue,
  });

  if (res.status == 200) {
    location.reload();
  }
}


async function generateChartData(){
    const res = await fetch(`http://127.0.0.1:8000/api/chartData`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken ,
    },
    });
    const jsonString = await res.text()
    if(res.status === 200){
        const parsedRes = JSON.parse(jsonString)
        $('#chart_user').val(parsedRes.user_count)
        $('#chart_car').val(parsedRes.car_count)
        $('#chart_rentalcar').val(parsedRes.rental_count)
        $('#chart_booking').val(parsedRes.booking_count)
        $('#chart_admin').val(parsedRes.admin_count)
        $('#chart_confirmation').val(parsedRes.confirmation_count)
        $('#chart_bill').val(parsedRes.bill_count)
    }
}

generateChartData()