import streamlit as st
import PyPDF2

#Para iniciar colocar en consola
#streamlit run unirpdf.py

def merge_pdfs(output_path, pdf_documents):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_document in pdf_documents:
        pdf_merger.append(pdf_document)
    
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

def main():
    st.image('assets/unirpdfs.png')
    st.header('Fusión de PDF')
    st.subheader('Adjunte archivos PDF para combinar')

    attached_pdfs = st.file_uploader(label='', accept_multiple_files=True, type=['pdf'])

    merge_button = st.button(label='Fusionar archivos PDF')

    if merge_button:
        if len(attached_pdfs) <= 1:
            st.warning('Adjunte más PDFs para fusionar')
        else:
            output_pdf = 'assets/pdf_final.pdf'
            
            # Leer los PDF adjuntos en formato binario
            pdf_files = [pdf.getbuffer() for pdf in attached_pdfs]
            merge_pdfs(output_pdf, pdf_files)
            
            st.success('Los archivos se fusionaron correctamente')

            with open(output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label='Descargar PDF fusionado', data=pdf_data, file_name='pdf_final.pdf')

if __name__ == '__main__':
    main()
