odoo.define('commerciale.firstjs', function (require){"user strict";
    console.log('verification du chargement')
    var core = require('web.core');
    var ListController = require('web.ListController');
    var _t = core._t;
    var Dialog = require('web.Dialog');
    var rpc = require('web.rpc');

    ListController.include({
        renderButtons: function($node) {
        this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.oe_action_button_factures').click(this.proxy('action_button'));
                }  
        },

        action_button: function () {
            console.log('verification du chargement tttttttttttttttttt')
            var dialog = new Dialog(document.body, {
            title: "Liste des factures",
            subtitle: "!",
            size: 'big',
            // rpcquery({
            //     model: 'commerciale.commandeclient',
            //     method: 'affiche_factures',
            // })
            
            })
            dialog.open();
            //alert('test alert !!!!!!!!')
        }

        

        
    })
});