const submitButton = document.querySelector("#submit");
const tableContainer = document.querySelector("#table-container");

submitButton.addEventListener("click", function(event) {
  event.preventDefault();
  const pickupPincode = document.querySelector("#pickup-pincode").value;
  const deliveryPincode = document.querySelector("#delivery-pincode").value;
  const weight = document.querySelector("#weight").value;

  const table = document.createElement("table");
  const thead = document.createElement("thead");
  const tbody = document.createElement("tbody");
  const headRow = document.createElement("tr");
  const headData1 = document.createElement("th");
  headData1.textContent = "Pickup Pincode";
  const headData2 = document.createElement("th");
  headData2.textContent = "Delivery Pincode";
  const headData3 = document.createElement("th");
  headData3.textContent = "Weight";
  const bodyRow = document.createElement("tr");
  const bodyData1 = document.createElement("td");
  bodyData1.textContent = pickupPincode;
  const bodyData2 = document.createElement("td");
  bodyData2.textContent = deliveryPincode;
  const bodyData3 = document.createElement("td");
  bodyData3.textContent = weight;

  headRow.appendChild(headData1);
  headRow.appendChild(headData2);
  headRow.appendChild(headData3);
  thead.appendChild(headRow);
  bodyRow.appendChild(bodyData1);
  bodyRow.appendChild(bodyData2);
  bodyRow.appendChild(bodyData3);
  tbody.appendChild(bodyRow);
  table.appendChild(thead);
  table.appendChild(tbody);
  tableContainer.appendChild(table);
});
