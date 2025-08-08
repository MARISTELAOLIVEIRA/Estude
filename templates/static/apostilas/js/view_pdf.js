const container = document.getElementById('pdf-container');
const data = document.currentScript.dataset;
const url = data.url

pdfjsLib.getDocument(url).promise.then(pdf => {
    pdf.getPage(1).then(page => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        const viewport = page.getViewport({ scale: 0.8 });

        canvas.width = viewport.width;
        canvas.height = viewport.height;

        page.render({ canvasContext: context, viewport }).promise.then(() => {
            container.appendChild(canvas);
        });
    });
});