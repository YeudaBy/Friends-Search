import { elastic as Menu } from 'react-burger-menu'
import React from 'react';
import { RiTelegramLine } from 'react-icons/ri';
import { VscCode } from "react-icons/vsc";
import { DiGithub } from "react-icons/di"
import { GoMention } from "react-icons/go"
import { useMediaPredicate } from "react-media-hook";
import SelectSiteLang from './SelectSiteLang';


export function NavBar(props) {

    return (
        <Menu >
            {/* <div className='itemsMenu'> */}
            <a id="home" className="menu-item" href="https://t.me/Friends_SearchBot">{<RiTelegramLine />} Telegram Bot</a>
            <a id="about" className="menu-item" href="https://github.com/YeudaBy/Friends-Search">{<DiGithub />} GitHub</a>
            <a id="contact" className="menu-item" href="https://api.friends-search.com">{<VscCode />} Api</a>
            <a className="menu-item" href="https://t.me/RobotTrickSupport">{<GoMention />} Contact </a>
            {/* </div> */}

            <SelectSiteLang updateLang={props.updateLang} className="siteSelectLang"/>
        </Menu>
    );

}