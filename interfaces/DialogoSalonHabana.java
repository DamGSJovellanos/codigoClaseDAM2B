/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package rojas_carrera_vincenzo_di01_tarea;

import javax.swing.*;
import javax.swing.border.TitledBorder;
import java.awt.*;
import java.util.Date;

/**
 *
 * @author DAM2B-11
 */


public class DialogoSalonHabana extends JDialog {

    private JTextField txtNombre, txtTelefono;
    private JSpinner spinnerFecha, spinnerPersonas, spinnerJornadas;
    private JComboBox<String> comboTipoEvento, comboCocina;
    private JCheckBox chkHabitaciones;
    private JButton btnConfirmar;

    public DialogoSalonHabana(Frame owner, boolean modal) {
        super(owner, "Reserva Salón Habana", modal);
        setSize(550, 600);
        setLocationRelativeTo(owner);
        setLayout(null);
        getContentPane().setBackground(new Color(240, 248, 255));

        // Imagen decorativa
        JLabel lblImagen = new JLabel(new ImageIcon(getClass().getResource("/imagenes/salonHabana.jpg")));
        lblImagen.setBounds(20, 10, 500, 120);
        add(lblImagen);

        // Panel Datos
        JPanel panelDatos = new JPanel(null);
        panelDatos.setBorder(new TitledBorder("Datos de contacto"));
        panelDatos.setBackground(new Color(255, 255, 255));
        panelDatos.setBounds(20, 140, 500, 100);

        JLabel lblNombre = new JLabel("Nombre:");
        lblNombre.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblNombre.setBounds(20, 25, 80, 25);
        txtNombre = new JTextField();
        txtNombre.setToolTipText("Introduce el nombre del contacto");
        txtNombre.setBounds(100, 25, 370, 25);

        JLabel lblTelefono = new JLabel("Teléfono:");
        lblTelefono.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblTelefono.setBounds(20, 60, 80, 25);
        txtTelefono = new JTextField();
        txtTelefono.setToolTipText("Introduce el teléfono (9 dígitos)");
        txtTelefono.setBounds(100, 60, 150, 25);

        panelDatos.add(lblNombre);
        panelDatos.add(txtNombre);
        panelDatos.add(lblTelefono);
        panelDatos.add(txtTelefono);
        add(panelDatos);

        // Panel Evento
        JPanel panelEvento = new JPanel(null);
        panelEvento.setBorder(new TitledBorder("Detalles del evento"));
        panelEvento.setBackground(new Color(255, 255, 255));
        panelEvento.setBounds(20, 260, 500, 250);

        JLabel lblFecha = new JLabel("Fecha del evento:");
        lblFecha.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblFecha.setBounds(20, 30, 130, 25);
        spinnerFecha = new JSpinner(new SpinnerDateModel());
        spinnerFecha.setEditor(new JSpinner.DateEditor(spinnerFecha, "dd/MM/yyyy"));
        spinnerFecha.setToolTipText("Selecciona la fecha del evento");
        spinnerFecha.setBounds(160, 30, 150, 25);

        JLabel lblTipo = new JLabel("Tipo de evento:");
        lblTipo.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblTipo.setBounds(20, 70, 130, 25);
        comboTipoEvento = new JComboBox<>(new String[]{"Banquete", "Jornada", "Congreso"});
        comboTipoEvento.setToolTipText("Selecciona el tipo de evento");
        comboTipoEvento.setBounds(160, 70, 150, 25);

        JLabel lblPersonas = new JLabel("Nº personas:");
        lblPersonas.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblPersonas.setBounds(20, 110, 130, 25);
        spinnerPersonas = new JSpinner(new SpinnerNumberModel(10, 1, 500, 1));
        spinnerPersonas.setToolTipText("Número de asistentes");
        spinnerPersonas.setBounds(160, 110, 80, 25);

        JLabel lblCocina = new JLabel("Tipo de cocina:");
        lblCocina.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblCocina.setBounds(20, 150, 130, 25);
        comboCocina = new JComboBox<>(new String[]{"Bufé", "Carta", "Pedir cita con el chef", "No precisa"});
        comboCocina.setToolTipText("Selecciona el tipo de cocina");
        comboCocina.setBounds(160, 150, 200, 25);

        JLabel lblJornadas = new JLabel("Nº jornadas:");
        lblJornadas.setFont(new Font("Segoe UI", Font.BOLD, 12));
        lblJornadas.setBounds(20, 190, 130, 25);
        spinnerJornadas = new JSpinner(new SpinnerNumberModel(1, 1, 10, 1));
        spinnerJornadas.setEnabled(false);
        spinnerJornadas.setBounds(160, 190, 80, 25);

        chkHabitaciones = new JCheckBox("Requiere habitaciones");
        chkHabitaciones.setFont(new Font("Segoe UI", Font.BOLD, 12));
        chkHabitaciones.setEnabled(false);
        chkHabitaciones.setBounds(260, 190, 180, 25);

        comboTipoEvento.addActionListener(e -> {
            boolean esCongreso = comboTipoEvento.getSelectedItem().equals("Congreso");
            spinnerJornadas.setEnabled(esCongreso);
            chkHabitaciones.setEnabled(esCongreso);
        });

        panelEvento.add(lblFecha);
        panelEvento.add(spinnerFecha);
        panelEvento.add(lblTipo);
        panelEvento.add(comboTipoEvento);
        panelEvento.add(lblPersonas);
        panelEvento.add(spinnerPersonas);
        panelEvento.add(lblCocina);
        panelEvento.add(comboCocina);
        panelEvento.add(lblJornadas);
        panelEvento.add(spinnerJornadas);
        panelEvento.add(chkHabitaciones);
        add(panelEvento);

        // Botón Confirmar
        btnConfirmar = new JButton("Confirmar Reserva");
        btnConfirmar.setToolTipText("Guarda la reserva del Salón Habana");
        btnConfirmar.setBounds(160, 530, 220, 35);
        btnConfirmar.setBackground(new Color(0, 153, 76));
        btnConfirmar.setForeground(Color.WHITE);
        btnConfirmar.setFont(new Font("Segoe UI", Font.BOLD, 14));
        btnConfirmar.addActionListener(e -> validarReserva());
        add(btnConfirmar);
    }

    private void validarReserva() {
        String nombre = txtNombre.getText().trim();
        String telefono = txtTelefono.getText().trim();
        Date fecha = (Date) spinnerFecha.getValue();

        if (nombre.isEmpty()) {
            JOptionPane.showMessageDialog(this, "El nombre es obligatorio.", "Error", JOptionPane.ERROR_MESSAGE);
            txtNombre.requestFocus();
            return;
        }
        if (!telefono.matches("\\d{9}")) {
            JOptionPane.showMessageDialog(this, "Introduce un teléfono válido de 9 dígitos.", "Error", JOptionPane.ERROR_MESSAGE);
            txtTelefono.requestFocus();
            return;
        }
        if (fecha.before(new Date())) {
            JOptionPane.showMessageDialog(this, "La fecha debe ser futura.", "Error", JOptionPane.ERROR_MESSAGE);
            spinnerFecha.requestFocus();
            return;
        }

        JOptionPane.showMessageDialog(this,
                "Reserva confirmada:\n" +
                "Nombre: " + nombre +
                "\nTeléfono: " + telefono +
                "\nEvento: " + comboTipoEvento.getSelectedItem() +
                "\nPersonas: " + spinnerPersonas.getValue() +
                "\nCocina: " + comboCocina.getSelectedItem(),
                "Reserva Exitosa", JOptionPane.INFORMATION_MESSAGE);
        dispose();
    }
}

