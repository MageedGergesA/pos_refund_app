odoo.define('pos_refund_employee_password.RefundPasswordButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");
    const TicketScreen = require('point_of_sale.TicketScreen');
    const rpc = require("web.rpc");

    const PosResTicketScreen1 = (TicketScreen) => class extends TicketScreen {
        async _onDoRefund() {
            const employee = this.env.pos.get_cashier();
            let global_refund = await rpc.query({
                model: 'ir.config_parameter',
                method: 'get_param',
                args: ["pos_refund_employee_password.global_refund_security"],
            });
//            console.log(global_refund)

            let refund = await rpc.query({
                model: 'hr.employee',
                method: 'get_pos_pswd',
                args: [employee.id,],
            });
//            console.log("refund", refund)

            if (global_refund){
                super._onDoRefund();
            } else {
                if (refund) {
                    const { confirmed, payload } = await this.showPopup('NumberPopup');
                    console.log("payload", payload)

                    if (refund == payload) {
                        super._onDoRefund();
                    } else {
                        this.showPopup('ErrorPopup', {
                            body: this.env._t('Invalid Password'),
                        });
                    }
                } else {
                        this.showPopup('ErrorPopup', {
                            body: this.env._t('You Need An Employee Refund Password'),
                        });
                }
            }
        }
    };

    Registries.Component.extend(TicketScreen, PosResTicketScreen1);
});
