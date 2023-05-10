/** @odoo-module **/
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

export class MachineStatus extends Component{
    setup(){
    this.state = useState({value:1})
    }
}
MachineStatus.template = 'machine_module.Machines'
registry.category('actions').add('machine_module.machine_status_screen_js', MachineStatus)



