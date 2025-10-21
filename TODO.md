0.01
- [ ] Bundle fonts like Chris SIL in flatpak
- [ ] Settings default:
      - [ ] 1. columns 2
      - [ ] 2. column gap 100
      - [ ] 3. margins all 4 100
      - [ ] 4. Font: Charis SIL
      - [ ] 5. Font size: 15
      - [ ] 6. Line spacing 1.50
      - [ ] 7. full justification
      
REading mode:      
BUGS:
  - [ ] gap 100 + Margin 100; columns not applying (just like Font)
  - [ ] gap 100 + Margin 100; columns not working for more than 5 perhaps due to gap
  - [ ] gap 100 + Margin 100; fixed width say 300 and resize to smaller when it becomes 1 column does not scroll
  - [ ] leafs are not properly scrolled in the webview on click
  - [ ] save current position on closing/clicking library button.
  - [ ] fixed width columns should also snap on resize, show/hide sidebar.
Features:
  - [ ] lower the height of toc items (expander and action row)
  - [ ] implement horizontal scrolling for 1 column along with vertical one. only when we select 1 column, if fixed width causes 1 column like using large pixel width or with huge gap and margin with fixed columns in a medium to small window.
  - [ ] like margins, we should have canvas size, so that irrespective of margins, if we select 2 columns it will show 2 columns with gap, much like foliate or margin left/right!?
  - [ ] next/previous should behave like page down/page; and when we reach at the end of a chapter; then behave like 'next/previous chapter' like is currently is.
  
  - [ ] invert/transfrom images for dark mode.
  - [ ] dark light css for text under light color like some epubs has.
  - [ ] using slider to show progress, and scroll with slider.
  - [ ] implement bookmarks
  - [ ] implement annotations with colors and text
  - [ ] implement voice changing and languge in tts tab.
  - [ ] stop tts on going to library, and exiting
  - [ ] start tts from 1st text from viewport.
  - [ ] font tab
        - [ ] refactor and show proper layout and options.
        
        - [ ] support reading style  
              - [ ] Newspaper 200px with 20 gap, 20 margins, font size 12 and 1.50 line space. (with hypernation)
              - [ ] Magazine  300px with 30 gap, 30 margins, font size 14, and 1.5 line space (full justification)
              - [ ] Foliate, size 20, use margins 150 left/right, 10/10 top/bottom; gap 150 fixed width 500
Features Library
  - [ ] Hamburger Menu -> Import epub from a directory. let the user select a dir to import all epubs into the library.
  - [ ] 1st launch library should show better view
  - [ ] Hamburger Menu -> Sort by A-Z, Z-A, Recency, Read percentage
  - [ ] Improve search show hide with esc. and position and size.
  - [ ] Bookmarks and Annotations should be accessible from card. search should search for bookmarks and annotations too.
library card:
  - [ ] percentage should be properly aligned (perhaps use center/right)
  
App Themes: Sepia, Solarized dark, atom one, etc.

- apply css to gtk and html; perhaps overaly colors?  
  
