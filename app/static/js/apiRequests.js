async function updateUserById() {
  const user_id = $("#modal_user_userid").val();
  const first_name = $("#modal_user_firstname").val();
  const last_name = $("#modal_user_lastname").val();
  const username = $("#modal_user_username").val();
  const password = $("#modal_user_password").val();
  const phone = $("#modal_user_phone").val();
  const email = $("#modal_user_email").val();

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
      phone: phone,
      email: email,
    }),
  });
  if (res.status == 200) {
    location.reload();
  }
}

async function updateBookingById() {
  const booking_id = $("#modal_booking_bookingid").val();
  const user_id = $("#modal_booking_userid").val();
  const rent_id = $("#modal_booking_rentid").val();
  const pickup_location = $("#modal_booking_pickuplocation").val();
  const dropoff_location = $("#modal_booking_dropofflocation").val();
  const pickup_date = $("#modal_booking_pickupdate").val();
  const dropoff_date = $("#modal_booking_dropoffdate").val();
  const pickup_time = $("#modal_booking_pickuptime").val();
  const dropoff_time = $("#modal_booking_dropofftime").val();

  const req_body = {
    booking_id,
    user_id,
    rent_id,
    pickup_location,
    dropoff_location,
    pickup_date,
    dropoff_date,
    pickup_time,
    dropoff_time,
  }
  console.log(req_body)

  const res = await fetch("http://127.0.0.1:8000/api/bookingById", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(req_body),
  });
  if (res.status == 200) {
    location.reload();
  }
}

async function updateConfirmById() {
  const booking_id = $("#modal_confirm_bookingid").val();
  const admin_id = $("#modal_confirm_adminid").val();
  const date = $("#modal_confirm_date").val();

  const res = await fetch("http://127.0.0.1:8000/api/confirmById", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      booking_id,
      admin_id,
      date
    }),
  });
  if (res.status == 200) {
    location.reload();
  }
}

async function updateBillById() {
  const bill_no = $("#modal_bill_billno").val();
  const booking_id = $("#modal_bill_bookingid").val();
  const total_fee = $("#modal_bill_totalfee").val();

  const res = await fetch("http://127.0.0.1:8000/api/billById", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      bill_no,
      booking_id,
      total_fee
    }),
  });
  if (res.status == 200) {
    location.reload();
  }
}

async function updateAdminById() {
  const admin_id = $("#modal_admin_adminid").val();
  const role = $("#modal_admin_role").val();

  const res = await fetch("http://127.0.0.1:8000/api/adminById", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      admin_id,
      role,
    }),
  });
  if (res.status == 200) {
    location.reload();
  }
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
    case "BOOKING":
      deleteLink = `${deleteLink}/bookingById`;
      reqBodyValue = JSON.stringify({
        booking_id: id,
      });
      break;
    case "ADMIN":
      deleteLink = `${deleteLink}/adminById`;
      reqBodyValue = JSON.stringify({
        admin_id: id,
      });
      break;
    case "CONFIRMATION":
      deleteLink = `${deleteLink}/confirmById`;
      reqBodyValue = JSON.stringify({
        booking_id: id,
      });
      break;
    case "BILL":
      deleteLink = `${deleteLink}/billById`;
      reqBodyValue = JSON.stringify({
        bill_no: id,
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

async function generateChartData() {
  const res = await fetch(`http://127.0.0.1:8000/api/chartData`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
  });
  const jsonString = await res.text();
  if (res.status === 200) {
    const parsedRes = JSON.parse(jsonString);
    $("#chart_user").val(parsedRes.user_count);
    $("#chart_car").val(parsedRes.car_count);
    $("#chart_rentalcar").val(parsedRes.rental_count);
    $("#chart_booking").val(parsedRes.booking_count);
    $("#chart_admin").val(parsedRes.admin_count);
    $("#chart_confirmation").val(parsedRes.confirmation_count);
    $("#chart_bill").val(parsedRes.bill_count);
  }
}

generateChartData();
