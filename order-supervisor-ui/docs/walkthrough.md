# Welcome to the Order Supervisor Dashboard!

If you are looking at this screen for the first time, don't worry. This guide is written in plain English to help you understand what this tool does, how it works, and how you can interact with it—even if you don't have a technical background.

---

## 🌟 The Big Picture: What is an "Order Supervisor"?

Imagine you run an online store. When a customer places an order, a lot of things happen behind the scenes:
1. They pay for the item.
2. The item is packaged.
3. A shipping courier picks it up.
4. The item is delivered to their doorstep.

Usually, everything goes smoothly. But sometimes, things go wrong: a card gets declined, the courier gets delayed in a snowstorm, or an angry customer demands a refund.

Normally, you would need a human support agent to watch every single order, send emails, call the delivery company, and handle complaints. 

The **Order Supervisor** is a smart digital assistant (an AI-powered virtual employee) that does this watching for you. It stays "asleep" when things are going fine, "wakes up" when there is a problem, takes action (like messaging the customer or delivery team), and logs everything it does.

---

## 🖥️ Tour of the Dashboard Layout

When you open [http://localhost:5173/](http://localhost:5173/) in your browser, you will see a clean dashboard divided into blocks:

1. **Control Center (Top Left):** This is your dashboard remote control. You can start the simulation, step through time hour-by-hour, reset it, or change safety limits.
2. **Supervisor State (Top Right):** Displays the current status of the order (e.g., active or closed), flags any active issues, and shows a quick text summary of what happened.
3. **Simulation Timeline (Bottom Left):** The history log. Every time the supervisor wakes up or takes an action, it logs it here.
4. **Communication Channels (Bottom Middle):** Shows what the customer or logistics team actually sees. You can toggle between WhatsApp messages, Email, and internal Slack logs.
5. **Human-in-the-Loop (Bottom Right):** Your control center! If the supervisor is about to do something high-risk (like refunding a large amount of money), it will stop and wait for your manual approval here.

---

## 🚀 Step-by-Step Guide: Running Your First Simulation

Let's walk through a real scenario of an order from payment to delivery.

### Step 1: Open the App
Go to [http://localhost:5173/](http://localhost:5173/) on your web browser. You will see the dashboard in its fresh, empty state.

### Step 2: Step Forward (Hour-by-Hour Playback)
Instead of running everything at once, click the **"Step Forward (0/0)"** button once.
* **What happens:** The simulation starts at **t = 0.0 hours** (when the order is placed).
* **The Scenario:** The payment fails because the card was declined.
* **The Supervisor's Action:** Since this is a problem, the supervisor wakes up, logs a note, and sends a comforting WhatsApp message to the customer: *"We noticed an issue with your payment -- retrying now..."*

### Step 3: Keep Stepping Through
Click **"Step Forward"** a few more times.
* **t = 0.5 hours:** Payment is successful! Since this is a routine event, the supervisor logs it but stays "asleep" to save energy and cost.
* **t = 1.0 hours:** Shipment is created. Again, this is normal, so it stays asleep.
* **t = 7.0, 13.0, and 19.0 hours:** There are no updates from the courier. But our supervisor doesn't just forget about the order! Every 6 hours, it wakes up on its own ("Synthetic check-in") to make sure nothing is stuck. Since the order is on track, it goes back to sleep.
* **t = 20.0 hours:** Oh no! The shipping team reports a delay due to a courier backlog. 
  * The supervisor wakes up.
  * It sends a WhatsApp warning to the customer.
  * It pings the courier logistics team on Slack demanding a new delivery time.
  * It sets a warning flag: **"openIssue: shipment_delayed"**.

### Step 4: The Angry Customer & Refund Request (Edge Cases)
Keep clicking **"Step Forward"**:
* **t = 40.0 hours:** The customer is frustrated and sends an angry message: *"This is ridiculous, I want a refund or I'm filing a chargeback."*
  * The supervisor detects angry keywords ("ridiculous", "chargeback") and flags the conversation. It replies politely: *"I'm sorry... looping in a specialist."*
* **t = 41.0 hours:** A refund request of **$2,600** is made.
  * Look at the **Human-in-the-Loop** card on the bottom right.
  * Because **$2,600** exceeds our safety limit of **$2,000**, the supervisor stops! It refuses to auto-approve it.
  * You will see two buttons light up: **"Approve Overlimit Refund"** or **"Decline & Escalate"**.
  * **Your Action:** Click **"Approve Overlimit Refund"**. You will see the supervisor record your manual approval and send the confirmation message.

### Step 5: Order Delivered
* **t = 70.0 hours:** The order is finally marked as delivered. The supervisor wakes up one last time, sends a cheerful *"hope you love it!"* delivery message, and permanently closes the workflow.

---

## ⚙️ Testing Custom Scenarios & Settings

You can play around with different settings to test how the system reacts:

### Scenario: Changing the Refund Limit
1. Locate the slider in the **Control Center** labeled "Refund Auto-Approve Limit".
2. Drag it to **$3,000**.
3. Click **"Run Full Simulation"** or step through again.
4. **What changes:** Since the refund request of $2,600 is now *under* your $3,000 threshold, the supervisor will auto-approve it without stopping to ask for your permission. You will see: *"Auto-approved refund of 2600 within policy limit"* in the logs!

### Resetting the Board
Any time you want to start over, simply click the **"Reset"** button to clear the logs and start back at hour zero.
