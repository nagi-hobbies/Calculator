import streamlit as st
import streamlit.components.v1 as stc
import sympy as sp

from latex2sympy import process_latex

st.title('Calculator')

'''
## target formula
'''

stc.html("""
         <script asyc>
         $(function(){
            $.ajax({
                url: 'test.py',
                type: 'post',
                data: 'massage'
            }).done(function(data){
                console.log(data);
            }).fail(function(){
                console.log('failed');
            });
        });
        </script>
         """)

tgt = st.text_input('')

st.latex(tgt)

x = sp.Symbol('x')

f = process_latex.process_sympy(tgt)

st.latex(sp.solve(f, x)[0])
