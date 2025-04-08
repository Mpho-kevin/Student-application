<!DOCTYPE html>
<html lang="en">
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>JEA Student Application Form</title>
  <!-- Other links and scripts here (Google Fonts, jsPDF, etc.) -->

  <!-- Place the success screen CSS here -->
  <style>
    /* Success Screen Styles */
    #successContainer {
      display: none;
      width: 100%;
      min-height: 100vh;
      background: linear-gradient(135deg, #87CEFA, #00BFFF);
      color: #fff;
      text-align: center;
      padding: 60px 20px;
      box-sizing: border-box;
    }
    #successContainer h2 {
      font-size: 2.5rem;
      margin-bottom: 20px;
      color: #fff;
    }
    #successContainer p {
      font-size: 1.2rem;
      margin-bottom: 30px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
    }
    #confettiCanvas {
      /* If you want a dedicated canvas area for confetti, define it here */
      width: 100%;
      height: 200px; /* Adjust as desired */
    }
    .success-buttons {
      margin-top: 20px;
    }
    .success-buttons button {
      background: #fff;
      color: #00BFFF;
      border: none;
      padding: 12px 30px;
      font-size: 1rem;
      border-radius: 6px;
      cursor: pointer;
      margin: 0 10px;
      transition: background 0.3s, color 0.3s;
    }
    .success-buttons button:hover {
      background: #00BFFF;
      color: #fff;
    }
  </style>
</head>
<body>
  <!-- Your existing multi-step form and successContainer elements here -->

  <!-- The rest of your code and scripts (multi-step logic, confetti, etc.) -->
</body>
</html>
  <style>
    /* Basic Reset */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    /* Background */
    body {
      font-family: 'Poppins', sans-serif;
      background: url("hd-educational-background.jpg") no-repeat center center fixed;
      background-size: cover;
      color: #333;
    }
    /* Main Form Container */
    .form-container {
      background: rgba(255, 255, 255, 0.95);
      border: 3px solid #87CEFA;
      border-radius: 15px;
      width: 90%;
      max-width: 700px;
      padding: 40px;
      margin: 40px auto;
      box-shadow: 0 10px 20px rgba(0,0,0,0.3);
      animation: fadeIn 1s ease;
      position: relative;
      z-index: 10;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.95); }
      to { opacity: 1; transform: scale(1); }
    }
    /* Logo */
    .logo { text-align: center; margin-bottom: 10px; }
    .logo img { max-width: 150px; }
    h2 { text-align: center; margin-bottom: 20px; color: #444; }
    /* Progress Bar */
    .progress-bar {
      display: flex;
      margin-bottom: 30px;
      counter-reset: step;
      justify-content: space-around;
    }
    .progress-step {
      flex: 1;
      position: relative;
      text-align: center;
      font-size: 12px;
      color: #aaa;
    }
    .progress-step::before {
      content: counter(step);
      counter-increment: step;
      width: 30px;
      height: 30px;
      line-height: 30px;
      border: 3px solid #ccc;
      display: block;
      text-align: center;
      margin: 0 auto 10px;
      border-radius: 50%;
      background-color: #fff;
    }
    .progress-step::after {
      content: '';
      position: absolute;
      width: 100%;
      height: 3px;
      background: #ccc;
      top: 15px;
      left: -50%;
      z-index: -1;
    }
    .progress-step:first-child::after { display: none; }
    .progress-step-active { color: #87CEFA; }
    .progress-step-active::before {
      border-color: #87CEFA;
      background-color: #87CEFA;
      color: #fff;
    }
    .progress-step-active::after { background-color: #87CEFA; }
    /* Form Steps */
    form { position: relative; }
    .form-step { display: none; animation: slideIn 0.5s ease forwards; }
    .form-step-active { display: block; }
    @keyframes slideIn {
      from { opacity: 0; transform: translateX(50px); }
      to { opacity: 1; transform: translateX(0); }
    }
    .input-group { margin-bottom: 15px; }
    .input-group label {
      display: block;
      margin-bottom: 5px;
      color: #555;
      font-weight: 600;
    }
    .input-group input,
    .input-group select,
    .input-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .button-group {
      display: flex;
      justify-content: space-between;
      margin-top: 20px;
    }
    .button-group button {
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      background: #87CEFA;
      color: #fff;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s ease;
    }
    .button-group button:hover { background: #00BFFF; }
    /* Package Cards */
    .package-card {
      border: 2px solid #ccc;
      border-radius: 8px;
      padding: 20px;
      text-align: center;
      cursor: pointer;
      transition: border 0.3s;
      margin-bottom: 15px;
      background: #fafafa;
    }
    .package-card.selected {
      transition: transform 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
    }
    .package-card:hover {
      transform: scale(1.05);
      border-color: #87CEFA;
      background-color: #e0f7ff;
    }
    /* Scheduling Styles */
    .schedule-header { margin-bottom: 15px; }
    .schedule-header p {
      font-size: 18px;
      margin-bottom: 5px;
      color: #333;
      font-weight: 600;
      display: flex;
      gap: 5px;
      align-items: center;
    }
    .schedule-header .label {
      color: #555;
      text-transform: uppercase;
      font-size: 14px;
      letter-spacing: 1px;
      font-weight: 500;
    }
    #scheduleContainer { margin-bottom: 20px; }
    .schedule-entry {
      background: #f0f9ff;
      border: 2px solid #87CEFA;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 15px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      transition: transform 0.2s ease;
    }
    .schedule-entry:hover { transform: translateY(-2px); }
    .schedule-entry label {
      display: block;
      margin-bottom: 8px;
      font-weight: 600;
      color: #333;
    }
    .schedule-entry select,
    .schedule-entry input[type="number"] {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      margin-bottom: 10px;
      border: 1px solid #87CEFA;
      border-radius: 4px;
      background: #fff;
      font-size: 14px;
      color: #333;
      transition: border-color 0.3s ease;
    }
    .schedule-entry select:focus,
    .schedule-entry input[type="number"]:focus {
      outline: none;
      border-color: #00BFFF;
    }
    .schedule-entry button {
      background: #e74c3c;
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: 6px 10px;
      cursor: pointer;
      transition: background 0.3s ease;
      font-size: 14px;
    }
    .schedule-entry button:hover { background: #c0392b; }
    .schedule-summary {
      margin-top: 20px;
      padding: 15px;
      background-color: #eef;
      border-radius: 6px;
      font-size: 14px;
      color: #333;
      line-height: 1.6;
    }
    /* Download PDF Button */
    .download-pdf-container {
      text-align: center;
      margin-top: 20px;
    }
    .download-pdf-container button {
      background: #87CEFA;
      border: none;
      color: #fff;
      padding: 12px 30px;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s ease, transform 0.2s ease;
    }
    .download-pdf-container button:hover {
      background: #00BFFF;
      transform: translateY(-2px);
    }
    /* Table Styling in Final Summary */
    table.schedule-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
      font-size: 14px;
    }
    table.schedule-table thead {
      background: #87CEFA;
      color: #fff;
    }
    table.schedule-table th,
    table.schedule-table td {
      border: 1px solid #ccc;
      padding: 8px;
      text-align: center;
    }
    table.schedule-table tbody tr:nth-child(even) {
      background: #f9f9f9;
    }
    /* Custom "Add a Day" Button */
    #addSchedule {
      display: inline-block;
      background: #87CEFA;
      color: #fff;
      padding: 12px 30px;
      font-size: 16px;
      font-weight: 600;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s ease, transform 0.2s ease;
      margin-bottom: 20px;
    }
    #addSchedule:hover {
      background: #00BFFF;
      transform: translateY(-2px);
    }
    /* Step 5: Review & Submit Styling */
    #step-5 h3 {
      margin-bottom: 15px;
      font-size: 20px;
      color: #444;
    }
    #finalSummary { margin-bottom: 20px; }

    /* Step 2: Center Previous Button and remove Next button */
    #step-2 .button-group {
      display: flex;
      justify-content: center;
    }
    #step-2 .btn-prev {
      margin: 0 auto;
    }
    #step-2 .btn-next {
      display: none;
    }

    /* ---------- Payment Container ---------- */
    .payment-container {
      background: #fff;
      max-width: 900px;
      width: 100%;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
      display: flex;
      flex-wrap: wrap;
      margin: 20px auto;
      animation: fadeIn 0.8s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.95); }
      to   { opacity: 1; transform: scale(1); }
    }
    /* ---------- Left Side: Amount Display ---------- */
    .amount-display {
      flex: 1;
      padding: 30px;
      background: linear-gradient(135deg, #87CEFA, #005f99);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      text-align: center;
    }
    .amount-display h2 {
      font-size: 2rem;
      margin-bottom: 10px;
    }
    /* ---------- Right Side: Payment Card/Form ---------- */
    .payment-card {
      flex: 2;
      padding: 30px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .payment-card h3 {
      text-align: center;
      margin-bottom: 20px;
      font-size: 1.5rem;
      color: #333;
    }
    /* ---------- Form Groups & Labels ---------- */
    .form-group {
      margin-bottom: 20px;
    }
    .form-label {
      display: block;
      margin-bottom: 8px;
      font-weight: 600;
      color: #444;
    }
    /* ---------- Card Input Wrapper ---------- */
    .card-input-wrapper {
      position: relative;
    }
    .card-input-wrapper input {
      width: 100%;
      padding: 12px 40px 12px 12px;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 1rem;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .card-input-wrapper input:focus {
      border-color: #87CEFA;
      box-shadow: 0 0 5px rgba(135, 206, 250, 0.5);
    }
    /* ---------- Card Brand Icon ---------- */
    .card-brand-icon {
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      display: flex;
      gap: 4px;
    }
    .card-brand-icon .circle {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background-color: #87CEFA;
    }
    /* ---------- Flex Row for Expiry and CVV ---------- */
    .flex-row {
      display: flex;
      gap: 10px;
    }
    .flex-row > * {
      flex: 1;
    }
    .flex-row select,
    .flex-row input[type="password"] {
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 1rem;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .flex-row select:focus,
    .flex-row input[type="password"]:focus {
      border-color: #87CEFA;
      box-shadow: 0 0 5px rgba(135, 206, 250, 0.5);
    }
    /* ---------- Pay Button ---------- */
    .pay-btn {
      width: 100%;
      background-color: #87CEFA;
      color: #fff;
      border: none;
      padding: 14px;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.3s ease, transform 0.3s ease;
      margin-top: 10px;
    }
    .pay-btn:hover {
      background-color: #00BFFF;
      transform: translateY(-2px);
    }
    /* ---------- Alternative Payment Methods ---------- */
    .payment-methods {
      margin-top: 30px;
    }
    .payment-methods h3 {
      margin-bottom: 15px;
      font-size: 1.2rem;
      text-align: center;
      color: #333;
    }
    .methods {
      display: flex;
      gap: 15px;
      justify-content: center;
      flex-wrap: wrap;
    }
    .methods button {
      background: #fff;
      color: #333;
      border: 1px solid #ccc;
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 0.9rem;
      cursor: pointer;
      transition: background 0.3s, transform 0.3s;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .methods button:hover {
      background: #f5f5f5;
      transform: translateY(-2px);
    }
    /* ---------- Previous Button Container ---------- */
    .btn-prev-container {
      text-align: center;
      width: 100%;
      margin: 20px 0;
    }
    .btn-prev {
      background: #87CEFA;
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s ease, transform 0.3s ease;
    }
    .btn-prev:hover {
      background: #00BFFF;
      transform: translateY(-2px);
    }
    /* ---------- Responsive Adjustments ---------- */
    @media (max-width: 768px) {
      .payment-container {
        flex-direction: column;
      }
      .amount-display, .payment-card {
        padding: 20px;
      }
      .amount-display h2 {
        font-size: 1.8rem;
      }

    }
  </style>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>JEA Student Application Form</title>
  <!-- Google Fonts: Using Poppins -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet" />
  <!-- jsPDF and AutoTable libraries for PDF generation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.23/jspdf.plugin.autotable.min.js"></script>
  <!-- Yoco SDK (use your public key in production) -->
  <script src="https://js.yoco.com/sdk/v1/yoco-sdk-web.js"></script>
  <!-- Canvas Confetti for celebration animation -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
</head>
<body>
  <!-- Main multi-step form container -->
  <div class="form-container">
    <!-- Logo and Title -->
    <div class="logo">
      <img src="Screenshot 2025-03-31 at 10.19.45.png" alt="JEA Logo" />
    </div>
    <h2>JEA Advanced Application Form</h2>
    <!-- Progress Bar -->
    <div class="progress-bar">
      <div class="progress-step progress-step-active" data-title="Personal"></div>
      <div class="progress-step" data-title="Package"></div>
      <div class="progress-step" data-title="Schedule"></div>
      <div class="progress-step" data-title="Start Day"></div>
      <div class="progress-step" data-title="Review & Submit"></div>
      <div class="progress-step" data-title="Payment"></div>
    </div>
    <form id="multiStepForm">
      <!-- Step 1: Personal Details -->
      <div class="form-step form-step-active" id="step-1">
        <div class="input-group">
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" placeholder="example@domain.com" required />
        </div>
        <div class="input-group">
          <label for="Gender">Student Gender:</label>
          <select id="Gender" name="Gender" required>
            <option value="" disabled selected>Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <div class="input-group">
          <label for="firstName">Student Name:</label>
          <input type="text" id="firstName" name="firstName" placeholder="John" required />
        </div>
        <div class="input-group">
          <label for="surname">Student Surname:</label>
          <input type="text" id="surname" name="surname" placeholder="Doe" required />
        </div>
        <div class="input-group">
          <label for="parentPhone">Parent Phone Number:</label>
          <input type="tel" id="parentPhone" name="parentPhone" placeholder="+27 123 456 789" required />
        </div>
        <div class="input-group">
          <label for="grade">Grade:</label>
          <input type="text" id="grade" name="grade" placeholder="10" required />
        </div>
        <div class="input-group">
          <label for="school">School:</label>
          <input type="text" id="school" name="school" placeholder="Your School Name" required />
        </div>
        
        <div class="button-group">
          <button type="button" class="btn-next">Next</button>
        </div>
      </div>
      
      <!-- Step 2: Package Selection -->
      <div class="form-step" id="step-2">
        <p>Please select a package:</p>
        <!-- 8 Hours Package (2 hours/week) -->
        <div class="package-card" data-package-id="pkg8hrs" data-hours="2" data-price="960" data-session-type="normal">
          <h3>8 Hours Package (Group Sessions)</h3>
          <p>R960</p>
          <p>Covers 2 hours/week</p>
        </div>
        <!-- 16 Hours Package (4 hours/week) -->
        <div class="package-card" data-package-id="pkg16hrs" data-hours="4" data-price="1500" data-session-type="normal">
          <h3>16 Hours Package(Group Sessions)</h3>
          <p>R1500</p>
          <p>Covers 4 hours/week</p>
        </div>
        <!-- Online Package (2 hours/week) -->
        <div class="package-card" data-package-id="pkgOnline2" data-hours="2" data-price="1200" data-session-type="normal">
          <h3>Online Package</h3>
          <p>R1200</p>
          <p> Covers 2 hours/week</p>
        </div>
        <!-- One on One Physical (2 hours/week) -->
        <div class="package-card" data-package-id="pkgPhysical2" data-hours="2" data-price="1600" data-session-type="physical">
          <h3>One on One (Physical)</h3>
          <p>R1600</p>
          <p>Covers 2 hours/week</p>
        </div>
        <!-- One on One Physical (4 hours/week) -->
        <div class="package-card" data-package-id="pkgPhysical4" data-hours="4" data-price="2950" data-session-type="physical">
          <h3>One on One (Physical)</h3>
          <p>R2950</p>
          <p>Covers 4 hours/week</p>
        </div>
        <input type="hidden" id="selectedPackageHours" name="selectedPackageHours" />
        <input type="hidden" id="selectedPackagePrice" name="selectedPackagePrice" />
        <div class="button-group">
          <button type="button" class="btn-prev">Previous</button>
          <button type="button" class="btn-next" id="toSchedule" disabled>Next</button>
        </div>
      </div>
      
      <!-- Step 3: Scheduling -->
      <div class="form-step" id="step-3">
        <div class="schedule-header">
          <p class="hours-text">
            <span class="label">Total Package Hours:</span>
            <span id="totalHours">0</span>
          </p>
          <p class="hours-text">
            <span class="label">Remaining Hours:</span>
            <span id="remainingHours">0</span>
          </p>
        </div>
        <div id="scheduleContainer">
          <!-- Schedule entries will appear here -->
        </div>
        <button type="button" id="addSchedule">Add a Day</button>
        <div class="schedule-summary" id="scheduleSummary">
          <!-- Schedule summary for the first week -->
        </div>
        <div class="button-group">
          <button type="button" class="btn-prev">Previous</button>
          <button type="button" class="btn-next" id="toStartDay" disabled>Next</button>
        </div>
      </div>
      
      <!-- Step 4: Starting Day -->
      <div class="form-step" id="step-4">
        <div class="input-group">
          <label for="startDay">Select Your Starting Day:</label>
          <input type="date" id="startDay" name="startDay" required />
        </div>
        <div class="button-group">
          <button type="button" class="btn-prev">Previous</button>
          <button type="button" class="btn-next">Next</button>
        </div>
      </div>
      
      <!-- Step 5: Review & Submit -->
      <div class="form-step" id="step-5">
        <h3>Review & Submit</h3>
        <p>Please review your application details before finishing.</p>
        <div id="finalSummary">
          <!-- Final summary info will appear here -->
        </div>
        <div class="download-pdf-container">
          <p>Would you like to download your schedule?</p>
          <button type="button" id="downloadPdfBtn">Download Schedule as PDF</button>
        </div>        
        <div class="button-group">
          <button type="button" class="btn-prev">Previous</button>
          <!-- Instead of proceeding to a payment step, this button triggers application success -->
          <button type="button" class="btn-next" id="submitApplicationBtn">Next</button>
        </div>
      </div>
    </form>
  </div>

  <!-- Success Screen (hidden by default) -->
  <div id="successContainer" style="display: none; text-align: center;">
    <h2>Application Successful!</h2>
    <p>
      We’ve sent your schedule to your email<br />
      Thank you for completing the JEA Application Form!
    </p>
    <div id="confettiCanvas"></div>
    <p>Would you like to submit another form?</p>
    <button id="newFormBtn">Yes</button>
    <button id="noFormBtn">No</button>
  </div>

  <!-- ----------------------- Script (JS Only, no CSS) ----------------------- -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {
  
      /***********************
       * NEW SCHOOL DROPDOWN CODE
       ***********************/
      // (School dropdown code remains unchanged)
      const allSchools = [
        "Akasia Hoërskool",
        "Amandasig Secondary School",
        "Assumption Convent School",
        "Boys’ High School, Pretoria",
        "Central Secondary School",
        "Chalton Vos College",
        "Clapham High School",
        "Crawford College, Bryanston",
        "Crawford College, Sandton",
        "Curro Academy Soshanguve",
        "Curro Midrand High School",
        "Eagle Christian College",
        "Hartebeespoort High School",
        "Hercules High School",
        "Hillview High School",
        "Hoërskool Alberton",
        "Hoërskool Ben Vorster",
        "Hoërskool Die Anker",
        "Hoërskool Eldoraigne",
        "Hoërskool FH Odendaal",
        "Hoërskool Garsfontein",
        "Hoërskool Gerrit Maritz",
        "Hoërskool Jan van Riebeeck",
        "Hoërskool Kempton Park",
        "Hoërskool Menlopark",
        "Hoërskool Overkruin",
        "Hoërskool Sandton",
        "Hoërskool Waterkloof",
        "Learskool Rachel de Beer",
        "Midstream College High School",
        "Mohlarutse Secondary School",
        "North Angelos Independent School",
        "Northwood High School",
        "Pelotona Secondary School",
        "Prestige College",
        "Pretoria Boys High School",
        "Pretoria High School for Girls",
        "PTH High School",
        "Redhill High School",
        "Rosina Sedibane Modiba Sports School",
        "Soshanguve East Secondary School",
        "St. Alban’s College",
        "St. John’s College",
        "St. Stithians College",
        "The Glen High School",
        "Think Digital Academy",
        "Victory Christian Learning Centre",
        "Voortrekker Eeufees Secondary School",
        "Waterkloof Primary School",
        "Xanadu Private School"
      ];
      allSchools.sort((a, b) => a.localeCompare(b));
      
      const schoolInput = document.getElementById("school");
      const schoolDropdown = document.createElement("div");
      schoolDropdown.id = "schoolDropdown";
      schoolDropdown.className = "school-dropdown";
      schoolDropdown.style.display = "none";
      schoolDropdown.style.position = "absolute";
      schoolDropdown.style.top = "100%";
      schoolDropdown.style.left = "0";
      schoolDropdown.style.right = "0";
      schoolDropdown.style.background = "#fff";
      schoolDropdown.style.border = "1px solid #ccc";
      schoolDropdown.style.maxHeight = "200px";
      schoolDropdown.style.overflowY = "auto";
      schoolDropdown.style.zIndex = "1000";
      
      const schoolInputParent = schoolInput.parentNode;
      if (window.getComputedStyle(schoolInputParent).position === "static") {
        schoolInputParent.style.position = "relative";
      }
      schoolInputParent.appendChild(schoolDropdown);
      
      schoolInput.addEventListener("input", () => {
        const query = schoolInput.value.toLowerCase().trim();
        const filtered = allSchools.filter(school =>
          school.toLowerCase().includes(query)
        );
        const groupedHTML = buildGroupedSchoolsHTML(filtered);
        if (groupedHTML) {
          schoolDropdown.innerHTML = groupedHTML;
          schoolDropdown.style.display = "block";
        } else {
          schoolDropdown.innerHTML = "";
          schoolDropdown.style.display = "none";
        }
      });
      
      document.addEventListener("click", (e) => {
        if (e.target !== schoolInput && !schoolDropdown.contains(e.target)) {
          schoolDropdown.style.display = "none";
        }
      });
      
      function buildGroupedSchoolsHTML(schools) {
        if (schools.length === 0) {
          return `<div style="padding: 10px; font-style: italic;">No matches found. <strong>Other</strong></div>`;
        }
        const groups = {};
        schools.forEach(school => {
          const letter = school.charAt(0).toUpperCase();
          if (!groups[letter]) {
            groups[letter] = [];
          }
          groups[letter].push(school);
        });
        let html = "";
        const letters = Object.keys(groups).sort();
        letters.forEach(letter => {
          html += `<div style="padding: 8px; border-bottom: 1px solid #eee;">
                     <div style="font-weight: bold; margin-bottom: 4px;">${letter}</div>
                     <ul style="list-style: none; padding: 0; margin: 0;">`;
          groups[letter].forEach(school => {
            html += `<li class="school-option" data-school="${school}" style="padding: 4px 0; cursor: pointer;">${school}</li>`;
          });
          html += `</ul>
                   </div>`;
        });
        html += `<div style="padding: 8px;">
                   <div style="font-weight: bold; margin-bottom: 4px;">Other</div>
                   <ul style="list-style: none; padding: 0; margin: 0;">
                     <li class="school-option" data-school="Other" style="padding: 4px 0; cursor: pointer;">Other</li>
                   </ul>
                 </div>`;
        return html;
      }
      
      schoolDropdown.addEventListener("click", (e) => {
        const clicked = e.target.closest(".school-option");
        if (clicked) {
          const chosenSchool = clicked.getAttribute("data-school");
          schoolInput.value = chosenSchool;
          schoolDropdown.style.display = "none";
        }
      });
      
      /***********************
       * EXISTING CODE (MULTI-STEP FORM, PACKAGE SELECTION, ETC.)
       ***********************/
      
      const form = document.getElementById("multiStepForm");
      const formSteps = document.querySelectorAll(".form-step");
      const btnNext = document.querySelectorAll(".btn-next");
      const btnPrev = document.querySelectorAll(".btn-prev");
      const progressSteps = document.querySelectorAll(".progress-step");
      
      let currentStep = 0;
      let totalPackageHours = 0;
      let remainingHours = 0;
      let scheduleData = [];
      
      const dayNameToNumber = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
      };
      
      btnNext.forEach(button => {
        button.addEventListener("click", () => {
          if (validateStep(currentStep)) {
            if (currentStep === 4) {
              processApplicationSuccess();
            } else {
              currentStep++;
              updateFormSteps();
              updateProgressBar();
              if (currentStep === 4) {
                updateFinalSummary();
              }
            }
          }
        });
      });
      
      btnPrev.forEach(button => {
        button.addEventListener("click", () => {
          // When leaving scheduling (Step 3) reset the "Add a Day" button
          if (currentStep === 2) {
            document.getElementById("addSchedule").disabled = false;
          }
          currentStep--;
          updateFormSteps();
          updateProgressBar();
        });
      });
      
      function updateFormSteps() {
        formSteps.forEach((formStep, index) => {
          formStep.classList.toggle("form-step-active", index === currentStep);
        });
      }
      
      function updateProgressBar() {
        progressSteps.forEach((progressStep, index) => {
          if (index <= currentStep) {
            progressStep.classList.add("progress-step-active");
          } else {
            progressStep.classList.remove("progress-step-active");
          }
        });
      }
      
      function validateStep(stepIndex) {
        const currentFormStep = formSteps[stepIndex];
        const inputs = currentFormStep.querySelectorAll("input, select, textarea");
        for (let input of inputs) {
          if (!input.checkValidity()) {
            input.reportValidity();
            return false;
          }
        }
        return true;
      }
    
        /***********************
         * PACKAGE SELECTION (STEP 2)
         ***********************/
        let currentSelectedPackage = null;
        const packageCards = document.querySelectorAll(".package-card");
        packageCards.forEach(card => {
          card.addEventListener("click", () => {
            const rawPrice = card.getAttribute("data-price");
            const numericPrice = Number(rawPrice.replace(/[^0-9.]/g, ''));
            localStorage.setItem("packagePrice", numericPrice);
    
            const newPackageId = card.getAttribute("data-package-id") || card.getAttribute("data-hours");
            if (currentSelectedPackage === newPackageId) {
              currentStep = 2;
              updateFormSteps();
              updateProgressBar();
              return;
            }
    
            packageCards.forEach(c => c.classList.remove("selected"));
            card.classList.add("selected");
    
            totalPackageHours = parseInt(card.getAttribute("data-hours"));
            remainingHours = totalPackageHours;
            document.getElementById("totalHours").innerText = totalPackageHours;
            document.getElementById("remainingHours").innerText = remainingHours;
            document.getElementById("selectedPackageHours").value = totalPackageHours;
            document.getElementById("selectedPackagePrice").value = rawPrice;
            document.getElementById("toSchedule").disabled = false;
    
            document.getElementById("scheduleContainer").innerHTML = '';
            document.getElementById("scheduleSummary").innerHTML = '';
            scheduleData = [];
    
            currentSelectedPackage = newPackageId;
            currentStep = 2;
            updateFormSteps();
            updateProgressBar();
          });
        });
    
        /***********************
         * SCHEDULING (STEP 3)
         ***********************/
        // Initially enable "Add a Day"
        document.getElementById("addSchedule").disabled = false;
        
        // Function to check whether the "Add a Day" button should be enabled.
        // It is enabled only if there are fewer than 2 entries and the last entry (if exists)
        // is complete and valid (hours must be exactly 2 or 4).
       // Function to check if the "Add a Day" button should be enabled.
function checkAddDayButton() {
  const addDayButton = document.getElementById("addSchedule");
  // Filter out removed (null) entries
  const validEntries = scheduleData.filter(entry => entry !== null);
  
  // If no valid entries exist, enable the button.
  if (validEntries.length === 0) {
    addDayButton.disabled = false;
    return;
  }
  
  // If one valid entry exists, enable the button only if that entry is complete.
  if (validEntries.length === 1) {
    const entry = validEntries[0];
    if (entry.subject && entry.day && entry.time && (entry.hours === 2 || entry.hours === 4)) {
      addDayButton.disabled = false;
    } else {
      addDayButton.disabled = true;
    }
    return;
  }
  
  // If two or more valid entries exist, disable the button.
  if (validEntries.length >= 2) {
    addDayButton.disabled = true;
  }
}

// Function to remove a schedule entry and re-check the add day button.
function removeScheduleEntry(id) {
  const entryDiv = document.querySelector(`[data-entry-id="${id}"]`);
  if (entryDiv) {
    // Remove the entry visually and mark its slot as null.
    entryDiv.remove();
    scheduleData[id] = null;
    updateRemainingHours();
    updateScheduleSummary();
    // Re-check the "Add a Day" button.
    checkAddDayButton();
  }
}

        
        document.getElementById("addSchedule").addEventListener("click", () => {
          if (remainingHours <= 0) {
            alert("You've allocated all available hours.");
            return;
          }
          // Check maximum entries (2 allowed)
          if (scheduleData.filter(entry => entry !== null).length >= 2) {
            alert("You can only add two days.");
            return;
          }
          checkAddDayButton();
          if (document.getElementById("addSchedule").disabled) {
            alert("Please complete the current schedule entry with 2 or 4 hours before adding another day.");
            return;
          }
          addScheduleEntry();
          checkAddDayButton();
          document.getElementById("toStartDay").disabled = false;
        });
    
        function getPhysicalAllowedDays() {
          return ["Friday", "Saturday"];
        }
        function getPhysicalAllowedTimes(day) {
          if (day === "Friday") {
            return ["15:00", "17:00"];
          } else if (day === "Saturday") {
            return ["13:00", "15:00"];
          }
          return [];
        }
        function getSubjectAllowedDays(subject) {
          switch(subject) {
            case "Mathematics":
            case "Mathematics Literacy":
              return ["Monday", "Tuesday", "Saturday"];
            case "Physics":
              return ["Wednesday", "Thursday", "Saturday"];
            case "Afrikaans":
            case "English":
              return ["Monday", "Tuesday", "Saturday"];
            default:
              return [];
          }
        }
        function getSubjectAllowedTimes(subject, day) {
          if (day !== "Saturday") {
            return ["15:00", "17:00"];
          } else {
            if (subject === "Mathematics" || subject === "Mathematics Literacy") {
              return ["09:00", "11:00"];
            } else if (subject === "Physics" || subject === "Afrikaans" || subject === "English") {
              return ["11:00", "13:00"];
            }
          }
          return [];
        }
        function isPhysicalPackage() {
          const selectedCard = document.querySelector(".package-card.selected");
          if (!selectedCard) return false;
          return selectedCard.getAttribute("data-session-type") === "physical";
        }
        
        function addScheduleEntry() {
          const entryId = scheduleData.length;
          const scheduleContainer = document.getElementById("scheduleContainer");
          const entryDiv = document.createElement("div");
          entryDiv.classList.add("schedule-entry");
          entryDiv.setAttribute("data-entry-id", entryId);
          entryDiv.innerHTML = `
            <label>Select Subject:
              <select class="schedule-subject" required>
                <option value="">-- Choose Subject --</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Mathematics Literacy">Mathematics Literacy</option>
                <option value="Physics">Physics</option>
                <option value="Afrikaans">Afrikaans</option>
                <option value="English">English</option>
              </select>
            </label>
            <label>Select Day:
              <select class="schedule-day" required>
                <option value="">-- Choose Subject First --</option>
              </select>
            </label>
            <label>Number of Hours (must be 2 or 4):
              <input type="number" class="schedule-hours" min="2" step="2" required>
            </label>
            <label>Select Start Time:
              <select class="schedule-time" required>
                <option value="">-- Choose Day First --</option>
              </select>
            </label>
            <button type="button" class="remove-btn">Remove</button>
          `;
          scheduleContainer.appendChild(entryDiv);
          
          // Add a new schedule entry object
          scheduleData.push({ subject: "", day: "", hours: 0, time: "" });
          
          const subjectSelect = entryDiv.querySelector(".schedule-subject");
          const daySelect = entryDiv.querySelector(".schedule-day");
          const hoursInput = entryDiv.querySelector(".schedule-hours");
          const timeSelect = entryDiv.querySelector(".schedule-time");
          const removeButton = entryDiv.querySelector(".remove-btn");
          
          subjectSelect.addEventListener("change", () => {
            scheduleData[entryId].subject = subjectSelect.value;
            // Reset day and time for a fresh start
            scheduleData[entryId].day = "";
            scheduleData[entryId].time = "";
            daySelect.innerHTML = '<option value="">-- Choose Day --</option>';
            timeSelect.innerHTML = '<option value="">-- Choose Day First --</option>';
            let allowedDays = [];
            if (isPhysicalPackage()) {
              allowedDays = getPhysicalAllowedDays();
            } else {
              allowedDays = getSubjectAllowedDays(subjectSelect.value);
            }
            allowedDays.forEach(d => {
              const opt = document.createElement("option");
              opt.value = d;
              opt.textContent = d;
              daySelect.appendChild(opt);
            });
            updateScheduleSummary();
            checkAddDayButton();
          });
          
          daySelect.addEventListener("change", () => {
            scheduleData[entryId].day = daySelect.value;
            scheduleData[entryId].time = "";
            timeSelect.innerHTML = '<option value="">-- Choose Time --</option>';
            let allowedTimes = [];
            if (isPhysicalPackage()) {
              allowedTimes = getPhysicalAllowedTimes(daySelect.value);
            } else {
              allowedTimes = getSubjectAllowedTimes(subjectSelect.value, daySelect.value);
            }
            // If another entry already uses the same day, filter out times already selected
            allowedTimes = allowedTimes.filter(timeOption => {
              return !scheduleData.some((entry, idx) => 
                idx !== entryId && entry && entry.day === daySelect.value && entry.time === timeOption
              );
            });
            allowedTimes.forEach(t => {
              const opt = document.createElement("option");
              opt.value = t;
              opt.textContent = t;
              timeSelect.appendChild(opt);
            });
            updateScheduleSummary();
            checkAddDayButton();
          });
          
          hoursInput.addEventListener("change", () => {
            let newVal = parseInt(hoursInput.value) || 0;
          
            // Validate hours must be exactly 2 or 4 (and not 0)
            if (newVal !== 2 && newVal !== 4) {
              alert("Hours must be exactly 2 or 4.");
              newVal = 0;
            }
            hoursInput.value = newVal;
            scheduleData[entryId].hours = newVal;
            updateRemainingHours();
            updateScheduleSummary();
            checkAddDayButton();
          });
          
          hoursInput.addEventListener("input", () => {
            let newVal = parseInt(hoursInput.value) || 0;
            if (newVal > remainingHours) {
              newVal = remainingHours;
            }
            hoursInput.value = newVal;
            scheduleData[entryId].hours = newVal;
            updateRemainingHours();
            updateScheduleSummary();
            checkAddDayButton();
          });
          
          timeSelect.addEventListener("change", () => {
            scheduleData[entryId].time = timeSelect.value;
            updateScheduleSummary();
            checkAddDayButton();
          });
          
          removeButton.addEventListener("click", () => {
            removeScheduleEntry(entryId);
            checkAddDayButton();
          });
        }
        
        function removeScheduleEntry(id) {
          const entryDiv = document.querySelector(`[data-entry-id="${id}"]`);
          if (entryDiv) {
            scheduleData[id].hours = 0;
            updateRemainingHours();
            entryDiv.remove();
            scheduleData[id] = null;
            updateScheduleSummary();
        
            // ✅ Check if all entries have been removed
            const hasEntriesLeft = scheduleData.some(entry => entry !== null && entry.hours > 0);
            
            // ✅ If nothing is left, allow the user to start over by enabling the button
            if (!hasEntriesLeft) {
              scheduleData = []; // clear scheduleData
              document.getElementById("addSchedule").disabled = false;
            }
        
            checkAddDayButton();
          }
        }
        
        
        function updateRemainingHours() {
          const allocated = scheduleData.reduce((sum, entry) => sum + (entry ? entry.hours : 0), 0);
          remainingHours = totalPackageHours - allocated;
          document.getElementById("remainingHours").innerText = remainingHours;
        }
        
        function updateScheduleSummary() {
          const summaryDiv = document.getElementById("scheduleSummary");
          const hasEntries = scheduleData.some(entry => entry && entry.subject && entry.day && entry.hours && entry.time);
        
          if (!hasEntries) {
            summaryDiv.innerHTML = "<strong>Schedule Summary (First Week):</strong><br>";
            return;
          }
        
          summaryDiv.innerHTML = "<strong>Schedule Summary (First Week):</strong><br>";
          scheduleData.forEach((entry, index) => {
            if (entry && entry.subject && entry.day && entry.hours && entry.time) {
              summaryDiv.innerHTML += `Entry ${index + 1}: ${entry.subject} on ${entry.day} for ${entry.hours} hour(s) starting at ${entry.time}<br>`;
            }
          });
        }
        
        
        /***********************
         * STEP 4: STARTING DAY LOGIC
         ***********************/
        const today = new Date();
        const isoToday = today.toISOString().split('T')[0];
        document.getElementById("startDay").min = isoToday;
        
        document.getElementById("startDay").addEventListener("change", function() {
          if (!this.value) return;
          const dateObj = new Date(this.value);
          const chosenDayNum = dateObj.getDay();
          const scheduledDays = getScheduledDayNumbers();
          if (!scheduledDays.has(chosenDayNum)) {
            alert("The chosen date does not match any scheduled day(s) in your schedule. Please pick a valid date.");
            this.value = "";
          }
        });
        
        function getScheduledDayNumbers() {
          const daySet = new Set();
          scheduleData.forEach((entry) => {
            if (entry && entry.day) {
              const dayNum = dayNameToNumber[entry.day];
              if (dayNum !== undefined) {
                daySet.add(dayNum);
              }
            }
          });
          return daySet;
        }
        
        /***********************
         * STEP 5: FINAL SUMMARY & PDF DOWNLOAD
         ***********************/
        function updateFinalSummary() {
          const summaryDiv = document.getElementById("finalSummary");
          const studentName = document.getElementById("firstName").value + " " + document.getElementById("surname").value;
          const grade = document.getElementById("grade").value;
          summaryDiv.innerHTML = `
            <h4>Student: ${studentName}</h4>
            <p>Grade: ${grade}</p>
            <h4>Review Your Application</h4>
          `;
          const email = document.getElementById("email").value;
          const parentPhone = document.getElementById("parentPhone").value;
          const school = document.getElementById("school").value;
          summaryDiv.innerHTML += `
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Parent Phone:</strong> ${parentPhone}</p>
            <p><strong>School:</strong> ${school}</p>
          `;
          const pkgHours = document.getElementById("selectedPackageHours").value;
          const pkgPrice = document.getElementById("selectedPackagePrice").value;
          summaryDiv.innerHTML += `<p><strong>Package:</strong> ${pkgHours} hour Package (R${pkgPrice})</p>`;
          summaryDiv.innerHTML += "<h4>Generated 4-Week Schedule:</h4>";
        
          const lessons = [];
          const startDay = document.getElementById("startDay").value;
          if (!startDay) return;
          const startDate = new Date(startDay);
          for (let week = 1; week <= 4; week++) {
            scheduleData.forEach(entry => {
              if (entry && entry.subject && entry.day && entry.hours && entry.time) {
                const targetDay = dayNameToNumber[entry.day];
                const startDayNumber = startDate.getDay();
                let offset = (targetDay - startDayNumber + 7) % 7;
                const lessonDate = new Date(startDate.getTime() + (offset + (week - 1) * 7) * 24 * 60 * 60 * 1000);
                lessons.push({
                  week: week,
                  subject: entry.subject,
                  day: entry.day,
                  lessonDate: lessonDate,
                  hours: entry.hours,
                  time: entry.time
                });
              }
            });
          }
          lessons.sort((a, b) => a.lessonDate - b.lessonDate);
        
          let tableHTML = `<table class="schedule-table">
                              <thead>
                                <tr>
                                  <th>Week</th>
                                  <th>Subject</th>
                                  <th>Day</th>
                                  <th>Date</th>
                                  <th>Hours</th>
                                  <th>Start Time</th>
                                </tr>
                              </thead>
                              <tbody>`;
          lessons.forEach(lesson => {
            const lessonDateStr = lesson.lessonDate.toISOString().split('T')[0];
            tableHTML += `<tr>
                            <td>Week ${lesson.week}</td>
                            <td>${lesson.subject}</td>
                            <td>${lesson.day}</td>
                            <td>${lessonDateStr}</td>
                            <td>${lesson.hours}</td>
                            <td>${lesson.time}</td>
                          </tr>`;
          });
          tableHTML += "</tbody></table>";
          summaryDiv.innerHTML += tableHTML;
          summaryDiv.innerHTML += `<p><strong>Starting Day:</strong> ${startDay}</p>`;
        }
        
        // PDF Download Functionality (Step 5)
        document.getElementById("downloadPdfBtn").addEventListener("click", downloadSchedulePDF);
        function downloadSchedulePDF() {
          try {
            console.log("downloadSchedulePDF called");
            const { jsPDF } = window.jspdf;
            if (!jsPDF) {
              console.error("jsPDF is not loaded.");
              return;
            }
            const doc = new jsPDF("p", "mm", "a4");
            const pageWidth = doc.internal.pageSize.getWidth();
            const pageHeight = doc.internal.pageSize.getHeight();
            console.log("PDF dimensions:", pageWidth, pageHeight);
        
            // Draw border around the page
            doc.setDrawColor(135, 206, 250);
            doc.setLineWidth(1);
            doc.rect(5, 5, pageWidth - 10, pageHeight - 10);
        
            // Add logo (replace with your actual Base64 string)
            const logoData = "data:image/png;base64,REPLACE_THIS_WITH_YOUR_BASE64_LOGO";
            try {
              doc.addImage(logoData, "PNG", 10, 10, 30, 30);
            } catch(e) {
              console.error("Error adding logo:", e);
            }
        
            // Add header texts
            const studentName = document.getElementById("firstName").value + " " + document.getElementById("surname").value;
            const grade = document.getElementById("grade").value;
            doc.setFont("helvetica", "bold");
            doc.setFontSize(14);
            doc.text(`Student: ${studentName}`, pageWidth / 2, 15, { align: "center" });
            doc.setFontSize(12);
            doc.setFont("helvetica", "normal");
            doc.text(`Grade: ${grade}`, pageWidth / 2, 25, { align: "center" });
        
            // Title
            doc.setFontSize(16);
            doc.setFont("helvetica", "bold");
            doc.text("JEA 4-Week Schedule", pageWidth / 2, 40, { align: "center" });
        
            // Build lessons array from scheduleData.
            // If scheduleData is empty, use fallback dummy data.
            const lessons = [];
            const startDayInput = document.getElementById("startDay").value;
            if (!startDayInput) {
              alert("No starting day selected. Using dummy starting day.");
            }
            const startDate = startDayInput ? new Date(startDayInput) : new Date();
            
            if (!scheduleData || scheduleData.filter(entry => entry !== null && entry.hours > 0).length === 0) {
              console.warn("No schedule data found. Using fallback dummy data.");
              // Create dummy data for one week
              lessons.push({
                week: 1,
                subject: "Mathematics",
                day: "Monday",
                lessonDate: new Date(startDate.getTime()),
                hours: 2,
                time: "15:00"
              });
              lessons.push({
                week: 1,
                subject: "Physics",
                day: "Tuesday",
                lessonDate: new Date(startDate.getTime() + 24 * 60 * 60 * 1000),
                hours: 2,
                time: "17:00"
              });
            } else {
              for (let week = 1; week <= 4; week++) {
                scheduleData.forEach(entry => {
                  if (entry && entry.subject && entry.day && entry.hours && entry.time) {
                    const targetDay = dayNameToNumber[entry.day];
                    const startDayNumber = startDate.getDay();
                    let offset = (targetDay - startDayNumber + 7) % 7;
                    const lessonDate = new Date(startDate.getTime() + (offset + (week - 1) * 7) * 24 * 60 * 60 * 1000);
                    lessons.push({
                      week: week,
                      subject: entry.subject,
                      day: entry.day,
                      lessonDate: lessonDate,
                      hours: entry.hours,
                      time: entry.time
                    });
                  }
                });
              }
            }
            lessons.sort((a, b) => a.lessonDate - b.lessonDate);
            console.log("Lessons array:", lessons);
        
            // Prepare table headers and body arrays
            const headers = [["Week", "Subject", "Day", "Date", "Hours", "Start Time"]];
            const body = lessons.map(lesson => {
              const lessonDateStr = lesson.lessonDate.toISOString().split("T")[0];
              return [
                "Week " + lesson.week,
                lesson.subject,
                lesson.day,
                lessonDateStr,
                lesson.hours.toString(),
                lesson.time
              ];
            });
        
            if (typeof doc.autoTable !== "function") {
              console.error("autoTable is not available. Please ensure jsPDF-AutoTable is loaded.");
              return;
            }
        
            doc.autoTable({
              head: headers,
              body: body,
              startY: 45,
              theme: "striped",
              headStyles: {
                fillColor: [135, 206, 250],
                textColor: [255, 255, 255],
                fontStyle: "bold"
              },
              margin: { left: 10, right: 10 }
            });
        
            // Add guidelines text below the table
            let finalY = doc.lastAutoTable ? doc.lastAutoTable.finalY + 15 : 80;
            doc.setFontSize(14);
            doc.setFont("helvetica", "bold");
            doc.setTextColor(135, 206, 250);
            doc.text("JEA Tutoring – Student Guidelines", pageWidth / 2, finalY, { align: "center" });
        
            finalY += 10;
            doc.setFontSize(11);
            doc.setFont("helvetica", "normal");
            doc.setTextColor(0, 0, 0);
            doc.setLineHeightFactor(1.4);
            const guidelines = [
              "• Be On Time – Arrive promptly and inform if late or absent.",
              "• Be Prepared – Bring all necessary materials.",
              "• Be Respectful – Treat tutors, staff, and peers with respect.",
              "• Be Honest – Do your own work.",
              "• Be Tidy – Keep your space clean.",
              "• Be Consistent – Regular attendance is key.",
              "• Be Safe – Follow safety guidelines.",
              "• Ask Questions – Stay engaged.",
              "• Keep Parents Informed – Progress reports are provided."
            ];
            guidelines.forEach((line, i) => {
              doc.text(line, pageWidth / 2, finalY + (i * 7), { align: "center" });
            });
        
            console.log("PDF generation complete. Saving PDF...");
            doc.save("JEA_Schedule.pdf");
          } catch (err) {
            console.error("Error in downloadSchedulePDF:", err);
          }
        }
    
        /***********************
         * APPLICATION SUCCESS & SAVE LOGIC
         ***********************/
        function processApplicationSuccess() {
          saveApplicationData();
          const applicantEmail = document.getElementById("email").value;
          sendEmailWithSchedule(applicantEmail);
          sendEmailWithSchedule("Je7academics@gmail.com");
          document.querySelector(".form-container").style.display = "none";
          document.getElementById("successContainer").style.display = "block";
          startConfetti();
        }
    
        function saveApplicationData() {
          const applicationData = {
            email: document.getElementById("email").value,
            firstName: document.getElementById("firstName").value,
            surname: document.getElementById("surname").value,
            parentPhone: document.getElementById("parentPhone").value,
            grade: document.getElementById("grade").value,
            school: document.getElementById("school").value,
            schedule: scheduleData,
            packagePrice: localStorage.getItem("packagePrice")
          };
          localStorage.setItem("latestApplication", JSON.stringify(applicationData));
          console.log("Application data saved:", applicationData);
        }
    
        function sendEmailWithSchedule(recipientEmail) {
          fetch("/send-email", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              to: recipientEmail,
              subject: "Your JEA Schedule",
              text: "Please find attached your schedule.",
            })
          })
          .then(res => res.json())
          .then(data => console.log("Email sent to:", recipientEmail))
          .catch(err => console.error("Error sending email:", err));
        }
    
        /***********************
         * CONFETTI ANIMATION
         ***********************/
        function startConfetti() {
          const duration = 5000;
          const animationEnd = Date.now() + duration;
          const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 1000 };
          function randomInRange(min, max) {
            return Math.random() * (max - min) + min;
          }
          const interval = setInterval(function() {
            const timeLeft = animationEnd - Date.now();
            if (timeLeft <= 0) {
              return clearInterval(interval);
            }
            const particleCount = 50 * (timeLeft / duration);
            confetti(Object.assign({}, defaults, {
              particleCount,
              origin: { x: randomInRange(0, 1), y: Math.random() - 0.2 }
            }));
          }, 250);
        }
    
        /***********************
         * NEW FORM SUBMISSION PROMPT
         ***********************/
      
        document.getElementById("noFormBtn").addEventListener("click", () => {
          alert("Thank you for your application!");
        });

        function processApplicationSuccess() {
          // Save application data locally
          saveApplicationData();
          
          // Retrieve the latest application data (saved via saveApplicationData)
          const applicationData = JSON.parse(localStorage.getItem("latestApplication"));
          
          // Retrieve existing applications or create a new array if none exists
          let studentsInformation = JSON.parse(localStorage.getItem("studentsInformation")) || [];
          
          // Append the current application data
          studentsInformation.push(applicationData);
          
          // Save the updated array back to localStorage
          localStorage.setItem("studentsInformation", JSON.stringify(studentsInformation));
          
          // Optionally send email notifications
          const applicantEmail = document.getElementById("email").value;
          sendEmailWithSchedule(applicantEmail);
          sendEmailWithSchedule("Je7academics@gmail.com");
          
          // Hide the form, show the success screen, start confetti animation
          document.querySelector(".form-container").style.display = "none";
          document.getElementById("successContainer").style.display = "block";
          startConfetti();
      
        }
        
        
      }); // End of DOMContentLoaded
    </script>
    
