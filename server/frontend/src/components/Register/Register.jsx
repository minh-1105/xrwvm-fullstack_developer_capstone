import React, { useState } from "react";

export default function Register() {
  const [form, setForm] = useState({
    username: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  const updateField = (event) => {
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const submitRegistration = (event) => {
    event.preventDefault();
    console.log("Register user", form);
  };

  return (
    <form className="register-form" onSubmit={submitRegistration}>
      <h1>Sign-Up</h1>
      <label htmlFor="username">Username</label>
      <input
        id="username"
        name="username"
        placeholder="Username"
        value={form.username}
        onChange={updateField}
        required
      />

      <label htmlFor="firstName">First Name</label>
      <input
        id="firstName"
        name="firstName"
        placeholder="First Name"
        value={form.firstName}
        onChange={updateField}
        required
      />

      <label htmlFor="lastName">Last Name</label>
      <input
        id="lastName"
        name="lastName"
        placeholder="Last Name"
        value={form.lastName}
        onChange={updateField}
        required
      />

      <label htmlFor="email">Email</label>
      <input
        id="email"
        name="email"
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={updateField}
        required
      />

      <label htmlFor="password">Password</label>
      <input
        id="password"
        name="password"
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={updateField}
        required
      />

      <button type="submit">Register</button>
    </form>
  );
}
