import React from 'react';
import Popup from 'reactjs-popup';
import "../App.css"

export default class Details extends React.Component {

  render() {
    return (
      <>
        <Popup
          trigger={<div className="openBtn"> Details </div>}
          modal
          nested
        >
          {close => (
            <div className="details">
              <button className="closeDetails" onClick={close}>
                &times;
              </button>
              <div className='content'>
                {this.props.res.content}
              </div>

            </div>
          )}
        </Popup>
      </>
    )
  }
}