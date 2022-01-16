/*! modernizr 3.11.2 (Custom Build) | MIT *
 * https://modernizr.com/download/?-cssanimations-csscolumns-customelements-flexbox-history-picture-pointerevents-postmessage-sizes-srcset-webgl-websockets-webworkers-addtest-domprefixes-hasevent-mq-prefixedcssvalue-prefixes-setclasses-testallprops-testprop-teststyles !*/ !function(e1, t1, n1, r1) {
    function o1(e, t) {
        return typeof e === t;
    }
    function i1(e) {
        var t = _.className, n = Modernizr._config.classPrefix || "";
        if (S && (t = t.baseVal), Modernizr._config.enableJSClass) {
            var r = new RegExp("(^|\\s)" + n + "no-js(\\s|$)");
            t = t.replace(r, "$1" + n + "js$2");
        }
        Modernizr._config.enableClasses && (e.length > 0 && (t += " " + n + e.join(" " + n)), S ? _.className.baseVal = t : _.className = t);
    }
    function s1(e, t) {
        if ("object" == typeof e) for(var n in e)k(e, n) && s1(n, e[n]);
        else {
            e = e.toLowerCase();
            var r = e.split("."), o = Modernizr[r[0]];
            if (2 === r.length && (o = o[r[1]]), void 0 !== o) return Modernizr;
            t = "function" == typeof t ? t() : t, 1 === r.length ? Modernizr[r[0]] = t : (!Modernizr[r[0]] || Modernizr[r[0]] instanceof Boolean || (Modernizr[r[0]] = new Boolean(Modernizr[r[0]])), Modernizr[r[0]][r[1]] = t), i1([
                (t && !1 !== t ? "" : "no-") + r.join("-")
            ]), Modernizr._trigger(e, t);
        }
        return Modernizr;
    }
    function a1() {
        return "function" != typeof n1.createElement ? n1.createElement(arguments[0]) : S ? n1.createElementNS.call(n1, "http://www.w3.org/2000/svg", arguments[0]) : n1.createElement.apply(n1, arguments);
    }
    function l1() {
        var e = n1.body;
        return e || (e = a1(S ? "svg" : "body"), e.fake = !0), e;
    }
    function u1(e, t, r, o) {
        var i, s, u, f, c = "modernizr", d = a1("div"), p = l1();
        if (parseInt(r, 10)) for(; r--;)u = a1("div"), u.id = o ? o[r] : c + (r + 1), d.appendChild(u);
        return i = a1("style"), i.type = "text/css", i.id = "s" + c, (p.fake ? p : d).appendChild(i), p.appendChild(d), i.styleSheet ? i.styleSheet.cssText = e : i.appendChild(n1.createTextNode(e)), d.id = c, p.fake && (p.style.background = "", p.style.overflow = "hidden", f = _.style.overflow, _.style.overflow = "hidden", _.appendChild(p)), s = t(d, e), p.fake ? (p.parentNode.removeChild(p), _.style.overflow = f, _.offsetHeight) : d.parentNode.removeChild(d), !!s;
    }
    function f1(e, n, r) {
        var o;
        if ("getComputedStyle" in t1) {
            o = getComputedStyle.call(t1, e, n);
            var i = t1.console;
            if (null !== o) r && (o = o.getPropertyValue(r));
            else if (i) {
                var s = i.error ? "error" : "log";
                i[s].call(i, "getComputedStyle returning null, its possible modernizr test results are inaccurate");
            }
        } else o = !n && e.currentStyle && e.currentStyle[r];
        return o;
    }
    function c1(e, t) {
        return !!~("" + e).indexOf(t);
    }
    function d1(e) {
        return e.replace(/([A-Z])/g, function(e, t) {
            return "-" + t.toLowerCase();
        }).replace(/^ms-/, "-ms-");
    }
    function p1(e2, n) {
        var o = e2.length;
        if ("CSS" in t1 && "supports" in t1.CSS) {
            for(; o--;)if (t1.CSS.supports(d1(e2[o]), n)) return !0;
            return !1;
        }
        if ("CSSSupportsRule" in t1) {
            for(var i = []; o--;)i.push("(" + d1(e2[o]) + ":" + n + ")");
            return i = i.join(" or "), u1("@supports (" + i + ") { #modernizr { position: absolute; } }", function(e) {
                return "absolute" === f1(e, null, "position");
            });
        }
        return r1;
    }
    function m(e) {
        return e.replace(/([a-z])-([a-z])/g, function(e, t, n) {
            return t + n.toUpperCase();
        }).replace(/^-/, "");
    }
    function h1(e, t, n, i) {
        function s() {
            u && (delete N.style, delete N.modElem);
        }
        if (i = !o1(i, "undefined") && i, !o1(n, "undefined")) {
            var l = p1(e, n);
            if (!o1(l, "undefined")) return l;
        }
        for(var u, f, d, h, A, v = [
            "modernizr",
            "tspan",
            "samp"
        ]; !N.style && v.length;)u = !0, N.modElem = a1(v.shift()), N.style = N.modElem.style;
        for(d = e.length, f = 0; f < d; f++)if (h = e[f], A = N.style[h], c1(h, "-") && (h = m(h)), N.style[h] !== r1) {
            if (i || o1(n, "undefined")) return s(), "pfx" !== t || h;
            try {
                N.style[h] = n;
            } catch (e) {
            }
            if (N.style[h] !== A) return s(), "pfx" !== t || h;
        }
        return s(), !1;
    }
    function A1(e, t) {
        return function() {
            return e.apply(t, arguments);
        };
    }
    function v1(e, t, n) {
        var r;
        for(var i in e)if (e[i] in t) return !1 === n ? e[i] : (r = t[e[i]], o1(r, "function") ? A1(r, n || t) : r);
        return !1;
    }
    function g(e, t, n, r, i) {
        var s = e.charAt(0).toUpperCase() + e.slice(1), a = (e + " " + O.join(s + " ") + s).split(" ");
        return o1(t, "string") || o1(t, "undefined") ? h1(a, t, r, i) : (a = (e + " " + T.join(s + " ") + s).split(" "), v1(a, t, n));
    }
    function y(e, t, n) {
        return g(e, r1, r1, t, n);
    }
    var w = [], C = {
        _version: "3.11.2",
        _config: {
            classPrefix: "",
            enableClasses: !0,
            enableJSClass: !0,
            usePrefixes: !0
        },
        _q: [],
        on: function(e, t) {
            var n = this;
            setTimeout(function() {
                t(n[e]);
            }, 0);
        },
        addTest: function(e, t, n) {
            w.push({
                name: e,
                fn: t,
                options: n
            });
        },
        addAsyncTest: function(e) {
            w.push({
                name: null,
                fn: e
            });
        }
    }, Modernizr = function() {
    };
    Modernizr.prototype = C, Modernizr = new Modernizr;
    var b = [], _ = n1.documentElement, S = "svg" === _.nodeName.toLowerCase(), x = "Moz O ms Webkit", T = C._config.usePrefixes ? x.toLowerCase().split(" ") : [];
    C._domPrefixes = T;
    var P = C._config.usePrefixes ? " -webkit- -moz- -o- -ms- ".split(" ") : [
        "",
        ""
    ];
    C._prefixes = P;
    var k;
    !function() {
        var e3 = {
        }.hasOwnProperty;
        k = o1(e3, "undefined") || o1(e3.call, "undefined") ? function(e, t) {
            return t in e && o1(e.constructor.prototype[t], "undefined");
        } : function(t, n) {
            return e3.call(t, n);
        };
    }(), C._l = {
    }, C.on = function(e, t) {
        this._l[e] || (this._l[e] = []), this._l[e].push(t), Modernizr.hasOwnProperty(e) && setTimeout(function() {
            Modernizr._trigger(e, Modernizr[e]);
        }, 0);
    }, C._trigger = function(e4, t) {
        if (this._l[e4]) {
            var n = this._l[e4];
            setTimeout(function() {
                var e;
                for(e = 0; e < n.length; e++)(0, n[e])(t);
            }, 0), delete this._l[e4];
        }
    }, Modernizr._q.push(function() {
        C.addTest = s1;
    });
    var E = function() {
        function e5(e, n) {
            var o;
            return !!e && (n && "string" != typeof n || (n = a1(n || "div")), e = "on" + e, o = e in n, !o && t && (n.setAttribute || (n = a1("div")), n.setAttribute(e, ""), o = "function" == typeof n[e], n[e] !== r1 && (n[e] = r1), n.removeAttribute(e)), o);
        }
        var t = !("onblur" in _);
        return e5;
    }();
    C.hasEvent = E;
    var B = function() {
        var e6 = t1.matchMedia || t1.msMatchMedia;
        return e6 ? function(t) {
            var n = e6(t);
            return n && n.matches || !1;
        } : function(e7) {
            var t = !1;
            return u1("@media " + e7 + " { #modernizr { position: absolute; } }", function(e) {
                t = "absolute" === f1(e, null, "position");
            }), t;
        };
    }();
    C.mq = B;
    var z = function(e, t) {
        var n = !1, r = a1("div"), o = r.style;
        if (e in o) {
            var i = T.length;
            for(o[e] = t, n = o[e]; (i--) && !n;)o[e] = "-" + T[i] + "-" + t, n = o[e];
        }
        return "" === n && (n = !1), n;
    };
    C.prefixedCSSValue = z;
    var O = C._config.usePrefixes ? x.split(" ") : [];
    C._cssomPrefixes = O;
    var L = {
        elem: a1("modernizr")
    };
    Modernizr._q.push(function() {
        delete L.elem;
    });
    var N = {
        style: L.elem.style
    };
    Modernizr._q.unshift(function() {
        delete N.style;
    }), C.testAllProps = g, C.testAllProps = y;
    C.testProp = function(e, t, n) {
        return h1([
            e
        ], r1, t, n);
    }, C.testStyles = u1;
    Modernizr.addTest("customelements", "customElements" in t1), Modernizr.addTest("history", function() {
        var e = navigator.userAgent;
        return !!e && (-1 === e.indexOf("Android 2.") && -1 === e.indexOf("Android 4.0") || -1 === e.indexOf("Mobile Safari") || -1 !== e.indexOf("Chrome") || -1 !== e.indexOf("Windows Phone") || "file:" === location.protocol) && t1.history && "pushState" in t1.history;
    });
    var R = [
        ""
    ].concat(T);
    C._domPrefixesAll = R, Modernizr.addTest("pointerevents", function() {
        for(var e = 0, t = R.length; e < t; e++)if (E(R[e] + "pointerdown")) return !0;
        return !1;
    });
    var j = !0;
    try {
        t1.postMessage({
            toString: function() {
                j = !1;
            }
        }, "*");
    } catch (e9) {
    }
    Modernizr.addTest("postmessage", new Boolean("postMessage" in t1)), Modernizr.addTest("postmessage.structuredclones", j), Modernizr.addTest("webgl", function() {
        return "WebGLRenderingContext" in t1;
    });
    var M = !1;
    try {
        M = "WebSocket" in t1 && 2 === t1.WebSocket.CLOSING;
    } catch (e8) {
    }
    Modernizr.addTest("websockets", M), Modernizr.addTest("cssanimations", y("animationName", "a", !0)), (function() {
        Modernizr.addTest("csscolumns", function() {
            var e = !1, t = y("columnCount");
            try {
                e = !!t, e && (e = new Boolean(e));
            } catch (e11) {
            }
            return e;
        });
        for(var e10, t2, n = [
            "Width",
            "Span",
            "Fill",
            "Gap",
            "Rule",
            "RuleColor",
            "RuleStyle",
            "RuleWidth",
            "BreakBefore",
            "BreakAfter",
            "BreakInside"
        ], r = 0; r < n.length; r++)e10 = n[r].toLowerCase(), t2 = y("column" + n[r]), "breakbefore" !== e10 && "breakafter" !== e10 && "breakinside" !== e10 || (t2 = t2 || y(n[r])), Modernizr.addTest("csscolumns." + e10, t2);
    })(), Modernizr.addTest("flexbox", y("flexBasis", "1px", !0)), Modernizr.addTest("picture", "HTMLPictureElement" in t1), Modernizr.addAsyncTest(function() {
        var e, t, n, r = a1("img"), o = "sizes" in r;
        !o && "srcset" in r ? (t = "data:image/gif;base64,R0lGODlhAgABAPAAAP///wAAACH5BAAAAAAALAAAAAACAAEAAAICBAoAOw==", e = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==", n = function() {
            s1("sizes", 2 === r.width);
        }, r.onload = n, r.onerror = n, r.setAttribute("sizes", "9px"), r.srcset = e + " 1w," + t + " 8w", r.src = e) : s1("sizes", o);
    }), Modernizr.addTest("srcset", "srcset" in a1("img")), Modernizr.addTest("webworkers", "Worker" in t1), (function() {
        var e, t, n, r, i, s, a;
        for(var l in w)if (w.hasOwnProperty(l)) {
            if (e = [], t = w[l], t.name && (e.push(t.name.toLowerCase()), t.options && t.options.aliases && t.options.aliases.length)) for(n = 0; n < t.options.aliases.length; n++)e.push(t.options.aliases[n].toLowerCase());
            for(r = o1(t.fn, "function") ? t.fn() : t.fn, i = 0; i < e.length; i++)s = e[i], a = s.split("."), 1 === a.length ? Modernizr[a[0]] = r : (Modernizr[a[0]] && (!Modernizr[a[0]] || Modernizr[a[0]] instanceof Boolean) || (Modernizr[a[0]] = new Boolean(Modernizr[a[0]])), Modernizr[a[0]][a[1]] = r), b.push((r ? "" : "no-") + a.join("-"));
        }
    })(), i1(b), delete C.addTest, delete C.addAsyncTest;
    for(var W = 0; W < Modernizr._q.length; W++)Modernizr._q[W]();
    e1.Modernizr = Modernizr;
}(window, window, document);

//# sourceMappingURL=index.74d88787.js.map
