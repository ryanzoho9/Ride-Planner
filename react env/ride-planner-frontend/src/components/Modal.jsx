import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

const Modal = ({ isOpen, onClose, children }) => {
  const [isMobile, setIsMobile] = useState(false);

  // Detect screen size to apply different animations
  useEffect(() => {
    const checkScreenSize = () => {
      setIsMobile(window.innerWidth <= 768);
    };

    checkScreenSize(); // Run initially
    window.addEventListener("resize", checkScreenSize); // Update on resize
    return () => window.removeEventListener("resize", checkScreenSize);
  }, []);

  if (!isOpen) return null;

  return (
    <AnimatePresence>
      <div
        className="modal-overlay"
        onClick={onClose} // Close modal when overlay is clicked
      >
        <motion.div
          className="modal-container"
          onClick={(e) => e.stopPropagation()} // Prevent closing when clicking inside modal
          initial={isMobile ? { opacity: 0, y: 100 } : { opacity: 0 }}
          animate={isMobile ? { opacity: 1, y: 0 } : { opacity: 1 }}
          exit={isMobile ? { opacity: 0, y: 100 } : { opacity: 0 }}
          transition={{ duration: 0.3 }}
        >
          {/* Close Button */}
          <button className="modal-close-button" onClick={onClose}>
            <img src="/assets/remove.svg" alt="Close" />
          </button>

          {/* Modal Content */}
          <div className="modal-content">{children}</div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
};

export default Modal;
