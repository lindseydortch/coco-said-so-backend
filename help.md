Header

import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { logout } from '../../actions/auth'

export class Header extends Component {
  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  }

  render() {
    const { isAuthenticated, user} = this.props.auth

    const authLinks = (
      <nav className="nav">
      <ul className="nav_list">
        <li className="nav_item">
          <Link onClick={this.props.logout}>
            Logout
          </Link>
        </li>
      </ul>
    </nav>

    );

    const guestLinks = (
      <nav className="nav">
        <ul className="nav_list">
          <li className="nav_item">
            <Link to="/register" className="nav_link">
              Register
            </Link>
          </li>
          <li className="nav_item">
            <Link to="/login" className="nav_link">
              Login
            </Link>
          </li>
        </ul>
      </nav>
    );

    return (
      <header className="header">
        <div className="logobar">
          <h1>
            COCO SAID SO
          </h1>
        </div>
        <div>
            {isAuthenticated ? authLinks : guestLinks}
        </div>
      </header>
    )
  }
}

const mapStateToProps = state => ({
  auth: state.auth
})

export default connect(mapStateToProps, { logout })(Header)

Main 
@import "base";

@import "layout/header.scss";
@import "layout/footer.scss";

@import "auth/login.scss";
@import "auth/register.scss";

Base
// ===========================================================
// VARIABLES 
// ===========================================================

// FONTS 
$logo-font: 'Raleway Dots', cursive;
$display-font: 'Raleway', sans-serif;

// COLORS 
$turqoise: #70D6ff;
$pink: #ff70a6;
$orange: #ff9770;
$yellow-dark: #ffd670;
$yellow-light: #e9ff70;

// ===========================================================
// BASIC STYLING
// ===========================================================
*, 
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

body {
  box-sizing: border-box;
  font-family: $display-font;
}

a {
  text-decoration: none;
  color: black;
}

package

    "watch:sass": "sass --watch sass/main.scss src/App.css"