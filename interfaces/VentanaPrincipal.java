/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package rojas_carrera_vincenzo_di01_tarea;

import javax.swing.*;
import java.awt.*;

/**
 *
 * @author DAM2B-11
 */

public class VentanaPrincipal extends JFrame {

    public VentanaPrincipal() {
        setTitle("Gestión Hotelera - BK");
        setSize(400, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(null);

        JMenuBar menuBar = new JMenuBar();
        JMenu menuReservas = new JMenu("Reservas");
        JMenuItem itemSalonHabana = new JMenuItem("Salón Habana");
        itemSalonHabana.addActionListener(e -> abrirDialogoSalon());
        menuReservas.add(itemSalonHabana);
        menuBar.add(menuReservas);
        setJMenuBar(menuBar);

        JLabel lblTitulo = new JLabel("Gestión de Salones BK", SwingConstants.CENTER);
        lblTitulo.setFont(new Font("Segoe UI", Font.BOLD, 18));
        lblTitulo.setBounds(50, 20, 300, 30);
        add(lblTitulo);

        JButton btnAbrir = new JButton("Reservar Salón Habana");
        btnAbrir.setToolTipText("Abre el formulario de reserva del Salón Habana");
        btnAbrir.setBounds(90, 90, 220, 40);
        btnAbrir.setBackground(new Color(0, 102, 204));
        btnAbrir.setForeground(Color.WHITE);
        btnAbrir.setFont(new Font("Segoe UI", Font.BOLD, 14));
        btnAbrir.addActionListener(e -> abrirDialogoSalon());
        add(btnAbrir);
    }

    private void abrirDialogoSalon() {
        DialogoSalonHabana dialogo = new DialogoSalonHabana(this, true);
        dialogo.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new VentanaPrincipal().setVisible(true));
    }
}

