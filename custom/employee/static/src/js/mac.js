/** @odoo-module **/
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

export class MacContainer extends Component{
    setup(){
    this.state = useState({value:1})
    }
}
MacContainer.template = 'employee.Mac'
registry.category('actions').add('employee.mac_js', MacContainer)



