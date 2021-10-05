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
    alert("Update Success");
    location.reload();
  }
}

async function deleteUserById(user_id){  
    const res = await fetch("http://127.0.0.1:8000/api/userById", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({
        user_id: user_id,
      }),
    });
    if (res.status == 200) {
      alert("DELETE SUCCESS");
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