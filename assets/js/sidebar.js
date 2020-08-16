/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace()

    $(".nav-link").click(function () {
        sessionStorage.setItem("active_menu", $(this).prop("id"))
    })
    $("#" + sessionStorage.getItem("active_menu")).addClass("active")
}())
