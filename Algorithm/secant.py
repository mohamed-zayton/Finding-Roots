from sympy import parse_expr, symbols


def secant_eq(equ, x_prev, x_curr, iter=50, prec=0.00005):
    x = symbols("x")    
    it_dic = {}
    fn = parse_expr(equ)
    num_of_iter = 0
    x_next = 0
    for i in range(iter):
        num_of_iter += 1
        f_x_curr = fn.subs(x, x_curr)
        f_x_prev = fn.subs(x, x_prev)
        x_next = round(x_curr - ((f_x_curr * (x_prev - x_curr))/(f_x_prev - f_x_curr)),6)
        calc_prec = abs((x_next-x_curr)/x_next) * 100
        if calc_prec < prec:
            it_dic[i] = [x_next, x_curr, x_prev, calc_prec]
            break
        it_dic[i] = [x_prev, x_next, x_curr, calc_prec]
        x_prev = x_curr
        x_curr = x_next


    return[it_dic, x_next, equ, iter, prec, num_of_iter,'secant']




# app = QtWidgets.QApplication(sys.argv)
# output_window = OutputWindow()
# output_window.set_iteration_value(res[3])
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(output_window)
# widget.resize(700,700)
# widget.show()
# sys.exit(app.exec_())

        


