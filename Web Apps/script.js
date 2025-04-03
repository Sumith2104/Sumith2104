
    const menu = {
      starters: [
        { name: "Chicken Curry", price: 200 },
        { name: "Chicken Kebab", price: 150 },
        { name: "Fish Fry", price: 190 },
        { name: "Mutton Curry", price: 300 }
      ],
      drinks: [
        { name: "Apple", price: 60 },
        { name: "Orange", price: 60 },
        { name: "Pineapple", price: 70 },
        { name: "Strawberry", price: 70 }
      ],
      nonveg: [
        { name: "Chicken Biryani", price: 400 },
        { name: "Special Chicken Biryani", price: 500 },
        { name: "Mutton Biryani", price: 650 },
        { name: "Special Mutton Biryani", price: 800 }
      ],
      veg: [
        { name: "Rice Sambar", price: 100 },
        { name: "North Indian Meals", price: 150 },
        { name: "South Indian Meals", price: 150 },
        { name: "Veg Pulao", price: 90 }
      ]
    };

    const selectedItems = {};
    let totalBill = 0;

    function populateMenu(section, items) {
      const sectionElem = document.getElementById(section);
      items.forEach(item => {
        const li = document.createElement('li');
        
        // Create a span for item name and price
        const itemName = document.createElement('span');
        itemName.textContent = `${item.name} - ₹${item.price}`;
        
        // Create a container for the quantity
        const quantityContainer = document.createElement('span');
        quantityContainer.id = `${item.name}-quantity`;
        quantityContainer.textContent = " (Qty: 0)";
        
        // Create the "Add" button
        const addButton = document.createElement('button');
        addButton.textContent = '+';
        addButton.onclick = () => addItemToBill(item.name, item.price, quantityContainer);

        // Create the "Delete" button
        const removeButton = document.createElement('button');
        removeButton.textContent = '-';
        removeButton.onclick = () => removeItemFromBill(item.name, item.price, quantityContainer);

        // Append the elements to the list item
        li.appendChild(itemName);
        li.appendChild(quantityContainer);
        li.appendChild(addButton);
        li.appendChild(removeButton);
        
        sectionElem.appendChild(li);
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      populateMenu('starters', menu.starters);
      populateMenu('drinks', menu.drinks);
      populateMenu('nonveg', menu.nonveg);
      populateMenu('veg', menu.veg);
    });

    function addItemToBill(itemName, price, quantityContainer) {
      totalBill += price;
      document.getElementById('total-bill').textContent = `Total Bill: ₹${totalBill}`;

      if (selectedItems[itemName]) {
        selectedItems[itemName].quantity += 1;
      } else {
        selectedItems[itemName] = { price: price, quantity: 1 };
      }

      quantityContainer.textContent = ` (Qty: ${selectedItems[itemName].quantity})`;
      displaySelectedItems();
    }

    function removeItemFromBill(itemName, price, quantityContainer) {
      if (selectedItems[itemName] && selectedItems[itemName].quantity > 0) {
        totalBill -= price;
        selectedItems[itemName].quantity -= 1;
        if (selectedItems[itemName].quantity === 0) delete selectedItems[itemName];
      }

      document.getElementById('total-bill').textContent = `Total Bill: ₹${totalBill}`;
      quantityContainer.textContent = ` (Qty: ${selectedItems[itemName] ? selectedItems[itemName].quantity : 0})`;
      displaySelectedItems();
    }

    function displaySelectedItems() {
      const selectedItemsDiv = document.getElementById('selected-items');
      selectedItemsDiv.innerHTML = "<h2>Selected Items</h2>";
      for (const item in selectedItems) {
        const itemDetail = selectedItems[item];
        const itemText = `${item} - ₹${itemDetail.price} x ${itemDetail.quantity} = ₹${itemDetail.price * itemDetail.quantity}`;
        const p = document.createElement('p');
        p.textContent = itemText;
        selectedItemsDiv.appendChild(p);
      }
    }

    function generateBill() {
      document.getElementById('total-bill').textContent = `Total Bill: ₹${totalBill}`;
      document.getElementById('qr-modal').style.display = 'flex';
      const qrCodeDiv = document.getElementById('qr-code');
      qrCodeDiv.innerHTML = "";

      const upiLink = `upi://pay?pa=sumithsumith4567890-1@oksbi&pn=ft_%20Sumith&am=${totalBill}&cu=INR&aid=uGICAgIC_nI3mVg`;
      new QRCode(qrCodeDiv, {
        text: upiLink,
        width: 128,
        height: 128,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
      });
    }

    function closeModal() {
      document.getElementById('qr-modal').style.display = 'none';

      // Prepare the bill content for download
      let billContent = `                   Hotel Bill\n`;
      billContent += `---------------------------------------------\n`;
      billContent += `Selected Items          Quantity        Price\n`;
      billContent += `---------------------------------------------\n`;

      for (const item in selectedItems) {
        const itemDetail = selectedItems[item];
        const itemLine = `${item.padEnd(20)}    ${itemDetail.quantity.toString().padEnd(10)}      ₹${(itemDetail.price * itemDetail.quantity).toString().padEnd(10)}\n`;
        billContent += itemLine;
      }

      billContent += `---------------------------------------------\n`;
      billContent += `Total Bill:                             ₹${totalBill}\n`;
      const blob = new Blob([billContent], { type: 'text/plain' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'hotel_bill.txt';
      link.click();
    }
  
function generateQRCode() {
    var qrElement = document.getElementById("qrcode");
    if (qrElement) {
        qrElement.innerHTML = "";
        new QRCode(qrElement, {
            text: "https://example.com",  // Change this URL as needed
            width: 128,
            height: 128
        });
    }
}

window.onload = generateQRCode;