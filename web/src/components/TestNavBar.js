import { elastic as Menu } from 'react-burger-menu'
import React from 'react';
import { FaTelegramPlane } from 'react-icons/fa';
import { VscCode } from "react-icons/vsc";
import { FiGithub } from "react-icons/fi"
import { GoMention } from "react-icons/go"
import { IoGameControllerOutline } from "react-icons/io5"
import SelectSiteLang from './SelectSiteLang';
import { BsInfoSquare } from "react-icons/bs" 
import { RiHome2Line } from "react-icons/ri"


export function NavBar(props) {

    return (
        <Menu >
            {/* <div className='itemsMenu'> */}
            <a className="menu-item" href="https://t.me/Friends_SearchBot">{<FaTelegramPlane />} Telegram Bot</a>
            <a className="menu-item" href="https://github.com/YeudaBy/Friends-Search">{<FiGithub />} GitHub</a>
            <a className="menu-item" href="https://api.friends-search.com">{<VscCode />} Api</a>
            <a className="menu-item" href="https://t.me/RobotTrickSupport">{<GoMention />} Contact </a>
            {<br />}
            <a className='menu-item' href='/'>{<RiHome2Line />} Home </a>
            <a className='menu-item' href='/game'>{<IoGameControllerOutline />} Game </a>
            <a className='menu-item' href='/about'>{<BsInfoSquare />} About </a>
            {/* </div> */}

            <SelectSiteLang updateSLang={props.updateSLang} className="siteSelectLang" sLang={props.sLang} />
        </Menu>
    );

}