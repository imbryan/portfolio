(function($) {
    $(document).ready(function() {
        const $field = $('#id_preview_text');
        const selector = "#preview-text-word-count";

        if ($field.attr('id') != "preview-text-wrapper") {
            $field.wrap('<div id="preview-text-wrapper"></div>');
        }

        $targetContainer = $field.parent();

        function updateWordCount() {
            const text = $field.val();
            const wordCount = text.trim().split(/\s+/).filter(word => word.length > 0).length;
            let msg = wordCount === 1 ? "word" : "words";
            if (wordCount > 50) {
                let over = wordCount - 50;
                msg = `${msg} (${over} over the limit)`;
            }
    
            let $display = $(selector);
            if (!$display.length) {
                const $newDisplay = $(`
                    <p style="text-align: right;">
                        <span id="preview-text-word-count"></span>
                    </p>    
                `);
                $targetContainer.append($newDisplay);
                $display = $(selector);
            }
    
            $display.text(`${wordCount} ${msg}`);
        }
        // Initialize word count
        updateWordCount();

        // Update word count on events
        $field.on('keyup change input', updateWordCount);
    });
})(django.jQuery);