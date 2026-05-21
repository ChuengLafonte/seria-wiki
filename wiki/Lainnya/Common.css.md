.slider-container {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.slider-images {
  display: flex;
  transition: transform 0.5s ease;
}

.slider-images img {
  width: 100%;
  flex-shrink: 0;
}

.slider-prev,
.slider-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.5);
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.slider-prev { left: 10px; }
.slider-next { right: 10px; }